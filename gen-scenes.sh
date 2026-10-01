#!/bin/bash
# Hook sahnelerini fal.ai flux/schnell ile uretir.
# Her sahne icin birkac aday -> assets/img/<id>-<n>.jpg
# Sonra elle en iyisini <id>.jpg olarak sec.
set -e
cd "$(dirname "$0")"
export FAL_KEY=$(python3 /tmp/_readfal.py)
[ -z "$FAL_KEY" ] && { echo "FAL_KEY okunamadi"; exit 1; }
mkdir -p assets/img

# Her sahnede tekrar eden karakter tanimi — tutarlilik icin sabit
CHAR="Simple hand-drawn stick figure cartoon, thick black outlines, plain white background, minimalist whiteboard-doodle style, flat colors, no shading, pink blush cheeks, childlike and charming, lots of white space. Recurring characters when present: MALE is a plain stick figure with a round circle head and no hair; FEMALE has shoulder-length brown hair and a blue dress."

SEED=7
CANDIDATES=3

gen () {
  local id="$1" scene="$2"
  echo ">> $id"
  for n in $(seq 1 $CANDIDATES); do
    local seed=$((SEED + n * 100))
    local resp=$(curl -s -m 120 -X POST "https://fal.run/fal-ai/flux/schnell" \
      -H "Authorization: Key $FAL_KEY" -H "Content-Type: application/json" \
      -d "{\"prompt\":\"$CHAR $scene\",\"image_size\":\"landscape_16_9\",\"num_images\":1,\"seed\":$seed}")
    local url=$(echo "$resp" | python3 -c "import sys,json;print(json.load(sys.stdin)['images'][0]['url'])" 2>/dev/null)
    if [ -n "$url" ]; then
      curl -s -m 60 "$url" -o "assets/img/$id-$n.jpg" && echo "   aday $n OK"
    else
      echo "   aday $n BASARISIZ: $(echo "$resp" | head -c 120)"
    fi
  done
}

# --- HOOK 15 sahne (basit, tek-eylemli promptlar daha iyi tutuyor) ---
gen L01 "A single plain stick figure man and a stick figure woman with brown hair and blue dress kissing, faces gently touching, standing together, empty white background."
gen L02 "A stick figure couple kissing in the center, while several plain identical stick figures walk past them on a grey sidewalk, a green cartoon tree and a grey street lamp in the background."
gen L03 "One single plain stick figure standing alone, looking at the viewer, empty white background."
gen L04 "A plain stick figure teacher next to a large empty blank whiteboard, pointing at the blank board with a stick, nothing written on it."
gen L05 "A single plain stick figure standing, looking puzzled and curious, question mark above the head, empty white background."
gen L06 "A simple cartoon globe of planet Earth with green continents and blue oceans, thick black outline, centered on white background."
gen L07 "A simple cartoon Earth globe with several small grey location pin dots scattered across the continents, white background."
gen L08 "A simple cartoon Earth globe with grey dots on the continents, a clipboard and pencil beside it, white background."
gen L09 "A simple cartoon Earth globe where a few of the location dots are highlighted bright orange and the rest stay grey, white background."
gen L10 "A mostly empty warm orange background, minimalist, nothing in the center, plenty of blank space."
gen L11 "A stick figure couple kissing on the left side, and a plain stick figure on the right making a disgusted grossed-out face, white background."
gen L12 "A close-up of a single plain stick figure face looking disgusted and grossed out, tongue slightly out, white background."
gen L13 "A single plain stick figure standing alone looking thoughtful, empty white background, lots of space."
gen L14 "A simple cartoon Earth globe with orange and grey dots, a big red question mark floating beside it, white background."
gen L15 "A plain stick figure looking curious with a thought bubble above the head containing a tiny kissing couple, white background."

echo "=== bitti ==="
ls assets/img/L*.jpg | wc -l | xargs echo "toplam aday:"
