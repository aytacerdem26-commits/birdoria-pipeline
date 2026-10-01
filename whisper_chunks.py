#!/usr/bin/env python3
"""Transcribe VO chunks via Groq Whisper, merge with offset correction."""
import os, json, requests, glob, subprocess

API_KEY = os.environ.get("GROQ_API_KEY", "")
CHUNK_DIR = "/Users/aytacerdem/zenn/inn_vo_chunks"
OUTPUT = "/Users/aytacerdem/zenn/inn_whisper_v2.json"

chunks = sorted(glob.glob(f"{CHUNK_DIR}/chunk_*.mp3"))
all_segments = []
all_words = []

for i, chunk_path in enumerate(chunks):
    # get chunk offset
    dur_cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration",
               "-of", "default=noprint_wrappers=1:nokey=1", chunk_path]

    # calculate offset: sum of all previous chunk durations
    offset = 0.0
    for j in range(i):
        prev = chunks[j]
        r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                           "-of", "default=noprint_wrappers=1:nokey=1", prev],
                          capture_output=True, text=True)
        offset += float(r.stdout.strip())

    print(f"[{i+1}/{len(chunks)}] {os.path.basename(chunk_path)} offset={offset:.1f}s ... ", end="", flush=True)

    with open(chunk_path, "rb") as f:
        resp = requests.post(
            "https://api.groq.com/openai/v1/audio/transcriptions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            files={"file": (os.path.basename(chunk_path), f, "audio/mpeg")},
            data=[
                ("model", "whisper-large-v3"),
                ("response_format", "verbose_json"),
                ("timestamp_granularities[]", "word"),
                ("timestamp_granularities[]", "segment"),
                ("language", "en"),
            ]
        )

    if resp.status_code != 200:
        print(f"FAIL ({resp.status_code})")
        print(resp.text[:500])
        continue

    data = resp.json()
    if not data:
        print(f"EMPTY response")
        continue

    # offset segments
    for seg in data.get("segments", []):
        seg["start"] += offset
        seg["end"] += offset
        all_segments.append(seg)

    # offset words
    for w in data.get("words", []):
        w["start"] += offset
        w["end"] += offset
        all_words.append(w)

    print(f"OK ({len(data.get('segments', []))} segments)")

result = {
    "text": " ".join(s.get("text", "").strip() for s in all_segments),
    "segments": all_segments,
    "words": all_words,
    "language": "en",
    "duration": all_segments[-1]["end"] if all_segments else 0
}

with open(OUTPUT, "w") as f:
    json.dump(result, f, indent=2)

print(f"\nDone! {len(all_segments)} segments, {len(all_words)} words saved to {OUTPUT}")
