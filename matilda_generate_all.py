#!/usr/bin/env python3
"""Generate all Matilda images via Nim API, 4 at a time, poll, download."""
import json, time, subprocess, os

PROMPTS_FILE = "/Users/aytacerdem/zenn/matilda_image_prompts.json"
RESULTS_FILE = "/Users/aytacerdem/zenn/matilda_image_results.json"
IMG_DIR = "/Users/aytacerdem/zenn/matilda_images"
MODEL_ID = "445ae371-607e-4e0c-b307-2115f5bcd4d2"

os.makedirs(IMG_DIR, exist_ok=True)

with open(PROMPTS_FILE) as f:
    prompts = json.load(f)

# Load existing results
if os.path.exists(RESULTS_FILE):
    with open(RESULTS_FILE) as f:
        results = json.load(f)
else:
    results = []

done_ids = {r["id"] for r in results if r.get("status") == "finished"}

# Skip already done, also skip first 4 (already submitted above)
# We'll handle first 4 separately
pending = [p for p in prompts if p["id"] not in done_ids]

print(f"Total: {len(prompts)}, Done: {len(done_ids)}, Pending: {len(pending)}")

# Nim MCP not available from script - use generate_image tool tracking
# This script will just track workflow IDs and poll/download
# For now, output the pending IDs
for p in pending:
    print(f"  [{p['id']}] {p['scene']}")
