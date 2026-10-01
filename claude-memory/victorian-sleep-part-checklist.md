---
name: victorian-sleep-part-checklist
description: "Victorian Sleep Stories per-part production checklist — full-clip verification + duration loop, run at the end of every visual-plan part"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d74244fa-a668-4547-9910-58b053b86bd3
  modified: 2026-09-03T22:15:55.932Z
---

At the end of EVERY part of a beekeeper/story visual plan (not just Part 1), before moving to the next part, do this for all stock clips sourced in that part:

1. **Full-clip verification, not single frame.** Extract a frame every ~1-2.5s across the whole clip (ffmpeg `fps=1,scale=...`), build a numbered contact-sheet grid, and Read it. A single mid-clip frame missed a car entering at t=9s, a satellite dish revealed mid-pan, and parked cars in later frames — multiple times. Reject or trim any clip with a modern element (cars, antennas, modern clothing/hands, modern signage) anywhere in its duration, not just the sampled frame.
2. **Duration-match every short clip.** Compare clip duration to the plan's target scene duration. For anything short, apply hard loop: `ffmpeg -y -stream_loop -1 -i input.mp4 -t <target> -c copy output.mp4`.

**Why:** User caught (twice) that single-frame checks and un-extended clips were shipping bad stock — modern cars/antennas hidden outside the sampled frame, and clips far shorter than their planned on-screen duration. Explicit instruction: run this checklist at the end of every part going forward, not just when reminded.

**How to apply:**
- Hard loop is the default duration-extension technique (validated against boomerang loop on scene_05: for near-static ambient shots the seam is imperceptible either way, and hard loop avoids the "motion reverses direction" artifact boomerang causes on directional content like flying bees or panning shots).
- Reserve boomerang loop (`reverse` + concat + stream_loop, see [[victorian-sleep-hybrid-production]]) only for clips with obvious one-direction motion where a hard cut would be jarring.
- AI stills (Nano Banana Lite) don't need this — Ken Burns handles their duration.
- This checklist is per-part, applied before reporting a part "done" to the user.
