#!/bin/bash
# HTML -> PNG (Chrome headless) -> MP4 (ffmpeg)
# Kullanim: ./render.sh
set -e

ROOT="$(cd "$(dirname "$0")" && pwd)"
OUT="$ROOT/out"
HTML="$OUT/html"
FRAMES="$OUT/frames"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

W=1920
H=1080

if [ ! -x "$CHROME" ]; then
  echo "HATA: Chrome bulunamadi: $CHROME"; exit 1
fi

mkdir -p "$FRAMES"
rm -f "$FRAMES"/*.png

LOG="$OUT/render.log"
: > "$LOG"

echo "1/4  HTML uretiliyor..."
node "$ROOT/build.js"

echo "2/4  Kareler render ediliyor..."
n=0
for f in "$HTML"/*.html; do
  base=$(basename "$f" .html)
  png="$FRAMES/$base.png"

  # Chrome'un stderr'i yutulmuyor; $LOG'a yaziliyor ki font/varlik
  # hatalari sessizce kaybolmasin.
  echo "--- $base ---" >> "$LOG"
  if ! "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
      --force-device-scale-factor=1 \
      --screenshot="$png" \
      --window-size=$W,$H \
      "file://$f" >>"$LOG" 2>&1; then
    echo ""
    echo "HATA: Chrome $base icin basarisiz oldu. Ayrinti: $LOG"; exit 1
  fi

  if [ ! -s "$png" ]; then
    echo ""
    echo "HATA: $base icin PNG uretilmedi ya da bos: $png"; exit 1
  fi

  n=$((n+1))
  printf "\r     %d kare" "$n"
done
echo ""

echo "3/4  Kareler dogrulaniyor..."
python3 "$ROOT/check-frames.py" "$FRAMES" || exit 1

echo "4/4  Video birlestiriliyor..."
cd "$OUT"
TARGET=$(cat "$OUT/duration.txt")

# Desktop iCloud senkronu altinda oldugu icin ffmpeg ara sira
# "Operation timed out" veriyor. 3 deneme hakki.
ok=0
for try in 1 2 3; do
  if ffmpeg -y -loglevel error \
      -f concat -safe 0 -i concat.txt \
      -t "$TARGET" \
      -vsync vfr -pix_fmt yuv420p \
      -vf "scale=$W:$H:flags=lanczos,fps=30" \
      -c:v libx264 -crf 18 -preset medium \
      "$OUT/video.mp4" >>"$LOG" 2>&1; then
    ok=1; break
  fi
  echo "     ffmpeg denemesi $try basarisiz, tekrar..."
  sleep 2
done

# 3 deneme de tukendiyse sessizce devam etmek yerine dur; yoksa bir
# sonraki adim eski/eksik video.mp4 uzerine ses bindirir.
if [ "$ok" -ne 1 ]; then
  echo "HATA: ffmpeg 3 denemede de basarisiz. Ayrinti: $LOG"
  tail -5 "$LOG"
  exit 1
fi

# ses varsa mux et
if [ -f "$OUT/audio-concat.txt" ]; then
  echo "     ses birlestiriliyor..."
  # mp3 parcalari -> aac (mp3'u m4a'ya -c copy ile kopyalamak basarisiz olur)
  ffmpeg -y -loglevel error -f concat -safe 0 -i audio-concat.txt -c:a aac -b:a 192k "$OUT/vo.m4a"
  ffmpeg -y -loglevel error -i "$OUT/video.mp4" -i "$OUT/vo.m4a" \
    -c:v copy -c:a aac -b:a 192k -shortest "$OUT/${TAG:-hook}.mp4"
  echo "     ses bindirildi"
else
  cp "$OUT/video.mp4" "$OUT/${TAG:-hook}.mp4"
  echo "     (ses yok — sessiz video)"
fi

dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT/${TAG:-hook}.mp4")
size=$(du -h "$OUT/${TAG:-hook}.mp4" | cut -f1)
echo ""
echo "TAMAM -> $OUT/${TAG:-hook}.mp4"
echo "Sure: ${dur}s | Boyut: $size | Kare: $n"
