#!/usr/bin/env python3
"""Split whisper segments into exactly 115 scenes."""
import json

NUM_SCENES = 115

with open("inn_whisper_v2.json") as f:
    w = json.load(f)

segments = w["segments"]
total_dur = segments[-1]["end"]
target_dur = total_dur / NUM_SCENES

# assign each segment to a scene based on its midpoint
scene_segments = [[] for _ in range(NUM_SCENES)]
for seg in segments:
    mid = (seg["start"] + seg["end"]) / 2
    scene_idx = min(int(mid / target_dur), NUM_SCENES - 1)
    scene_segments[scene_idx].append(seg)

scenes = []
for i in range(NUM_SCENES):
    segs = scene_segments[i]
    if segs:
        start = segs[0]["start"]
        end = segs[-1]["end"]
        text = " ".join(s.get("text", "").strip() for s in segs)
    else:
        # empty scene — interpolate
        start = i * target_dur
        end = (i + 1) * target_dur
        text = ""

    scenes.append({
        "id": i + 1,
        "start": round(start, 2),
        "end": round(end, 2),
        "duration": round(end - start, 2),
        "text": text[:200],
        "full_text": text
    })

with open("inn_scene_plan_v2.json", "w") as f:
    json.dump(scenes, f, indent=2)

durs = [s['duration'] for s in scenes]
print(f"{len(scenes)} scenes")
print(f"Duration range: {min(durs):.1f} - {max(durs):.1f}s, avg: {sum(durs)/len(durs):.1f}s")
print(f"Total: {sum(durs):.1f}s")
empties = sum(1 for s in scenes if not s['full_text'])
if empties:
    print(f"Warning: {empties} empty scenes")
