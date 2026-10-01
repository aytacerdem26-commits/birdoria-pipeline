#!/bin/bash
# Brian'in sesini Zenn temposuna getirir.
#   1) duraklamalari kirp (17.8% sessizlik -> ~%5)
#   2) hafif hizlandir (pitch bozulmaz)
#
# Kullanim: ./pace.sh girdi.mp3 cikti.mp3 [tempo]
#           tempo varsayilan 1.18
set -e

IN="$1"
OUT="$2"
TEMPO="${3:-1.18}"
KEEP="${KEEP_SILENCE:-0.18}"   # her duraklamadan korunacak sessizlik (sn)

if [ -z "$IN" ] || [ -z "$OUT" ]; then
  echo "kullanim: ./pace.sh girdi.mp3 cikti.mp3 [tempo]"; exit 1
fi

ffmpeg -y -loglevel error -i "$IN" -af "\
silenceremove=stop_periods=-1:stop_duration=${KEEP}:stop_threshold=-32dB:detection=rms,\
atempo=${TEMPO},\
loudnorm=I=-16:TP=-1.5:LRA=11" \
  -c:a libmp3lame -b:a 128k "$OUT"

d_in=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
d_out=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT")
printf "%s -> %s | %.1fs -> %.1fs (x%.2f kisalma)\n" \
  "$(basename "$IN")" "$(basename "$OUT")" "$d_in" "$d_out" \
  "$(echo "scale=3; $d_in/$d_out" | bc)"
