#!/usr/bin/env python3
"""Ken Burns montage: 115 scene images → video synced to VO timecodes."""

import json
import subprocess
import os
import sys

BASE = "/Users/aytacerdem/zenn"
IMG_DIR = f"{BASE}/inn_images"
CLIP_DIR = f"{BASE}/inn_clips"
SCENE_PLAN = f"{BASE}/inn_scene_plan_v2.json"
VO_FILE = f"{BASE}/inn_vo_v2.mp3"
OUTPUT = f"{BASE}/inn_final_video.mp4"
CONCAT_LIST = f"{BASE}/inn_concat.txt"

FPS = 30
W, H = 1920, 1080

os.makedirs(CLIP_DIR, exist_ok=True)

with open(SCENE_PLAN) as f:
    scenes = json.load(f)

def ken_burns_filter(idx, duration, fps=30):
    """4 motion presets cycling by index."""
    frames = int(duration * fps)
    if frames < 2:
        frames = 2
    preset = idx % 4
    if preset == 0:  # zoom in center
        return (
            f"scale=5760:-2,"
            f"zoompan=z='min(1.15,1+0.15*on/{frames})':"
            f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s={W}x{H}:fps={fps},"
            f"setsar=1,format=yuv420p"
        )
    elif preset == 1:  # zoom out center
        return (
            f"scale=5760:-2,"
            f"zoompan=z='max(1.0,1.15-0.15*on/{frames})':"
            f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s={W}x{H}:fps={fps},"
            f"setsar=1,format=yuv420p"
        )
    elif preset == 2:  # pan left to right
        return (
            f"scale=5760:-2,"
            f"zoompan=z='1.08':"
            f"x='(iw-iw/zoom)*on/{frames}':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s={W}x{H}:fps={fps},"
            f"setsar=1,format=yuv420p"
        )
    else:  # pan right to left
        return (
            f"scale=5760:-2,"
            f"zoompan=z='1.08':"
            f"x='(iw-iw/zoom)*(1-on/{frames})':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s={W}x{H}:fps={fps},"
            f"setsar=1,format=yuv420p"
        )

total = len(scenes)
for i, scene in enumerate(scenes):
    sid = scene["id"]
    dur = scene["duration"]
    img = f"{IMG_DIR}/scene_{sid:03d}.jpg"
    clip = f"{CLIP_DIR}/clip_{sid:03d}.mp4"

    if os.path.exists(clip):
        existing_dur = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", clip],
            capture_output=True, text=True
        )
        if existing_dur.returncode == 0:
            edur = float(existing_dur.stdout.strip())
            if abs(edur - dur) < 0.5:
                print(f"[{i+1}/{total}] clip_{sid:03d} exists ({edur:.1f}s), skip")
                continue

    vf = ken_burns_filter(sid - 1, dur, FPS)
    cmd = [
        "ffmpeg", "-y", "-loop", "1", "-i", img,
        "-t", str(dur), "-r", str(FPS),
        "-vf", vf,
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-pix_fmt", "yuv420p",
        clip
    ]
    print(f"[{i+1}/{total}] scene {sid}: {dur:.1f}s ... ", end="", flush=True)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"FAIL")
        print(result.stderr[-500:])
        sys.exit(1)
    print("OK")

# concat list
with open(CONCAT_LIST, "w") as f:
    for scene in scenes:
        sid = scene["id"]
        f.write(f"file '{CLIP_DIR}/clip_{sid:03d}.mp4'\n")

print(f"\nAll {total} clips ready. Concatenating + adding VO...")

concat_cmd = [
    "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", CONCAT_LIST,
    "-i", VO_FILE,
    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
    "-shortest",
    OUTPUT
]
result = subprocess.run(concat_cmd, capture_output=True, text=True)
if result.returncode != 0:
    print("CONCAT FAIL")
    print(result.stderr[-500:])
    sys.exit(1)

size_mb = os.path.getsize(OUTPUT) / (1024*1024)
print(f"\nDone! {OUTPUT} ({size_mb:.0f} MB)")
