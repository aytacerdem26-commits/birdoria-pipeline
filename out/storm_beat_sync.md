# Storm Video — Beat Sync (real VO timecodes)
# Source: storm_vo.mp3 (367.5s) via Groq Whisper large-v3 (57 seg / 901 words)
# Beat starts = actual narration timestamps, not estimates.

| Beat | Start | End | Dur | Images | sec/img |
|------|-------|-----|-----|--------|---------|
| COLD-OPEN | 0.0 | 52.0 | 52.0 | 01–10 | 5.20 |
| BEAT1 barometric | 52.0 | 105.5 | 53.5 | 11–18 | 6.69 |
| BEAT2 chickadee | 105.5 | 156.5 | 51.0 | 19–28 | 5.10 |
| BEAT3 cardinal | 156.5 | 210.0 | 53.5 | 29–37 | 5.94 |
| BEAT4 crow | 210.0 | 249.3 | 39.3 | 38–45 | 4.91 |
| BEAT5 owl | 249.3 | 298.0 | 48.7 | 46–54 | 5.41 |
| CLOSE | 298.0 | 367.5 | 69.5 | 55–68 | 4.97 |

## Drift vs manifest estimate
- Estimates were tight. Only real corrections:
  - **CROW shorter** — 39.3s (est 45). Images 38–45 pack tighter (~4.9s each).
  - **CLOSE longer** — 69.5s (est 57). 14 images at ~5.0s each.
- All beats land in healthy Ken Burns range (4.9–6.7 s/img). No re-scripting needed.

## Per-image timecodes
- Full list in `storm_image_times.csv` (img, start_s, dur_s, beat) — images evenly spaced inside each real beat window, order preserved.
- Feed directly into ffmpeg concat: set each clip duration = dur_s, stretch via setpts if beat-exact sync needed.

## Anchor phrases (for manual scrub verify)
- 0.0 "A storm is coming"
- 52.0 "Start with how they knew"
- 105.5 "Now the chickadee, the smallest"
- 156.5 "The cardinal takes a different route"
- 210.0 "The crow does not ride it out alone"
- 249.3 "And then there is the one that does not hide"
- 298.0 "Then it passes"
- ~360 "Tell me in the comments" (CTA)

## Files
- storm_vo_whisper.json — full word+segment timing
- storm_image_times.csv — per-image cut sheet
