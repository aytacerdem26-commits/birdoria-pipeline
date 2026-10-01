import json, time, subprocess, os

PROMPTS_FILE = "/Users/aytacerdem/zenn/inn_image_prompts_v2.json"
RESULTS_FILE = "/Users/aytacerdem/zenn/inn_image_results.json"
IMAGES_DIR = "/Users/aytacerdem/zenn/inn_images"
MODEL_ID = "445ae371-607e-4e0c-b307-2115f5bcd4d2"
BATCH_SIZE = 4
POLL_INTERVAL = 15

# Load env
env_path = os.path.expanduser("~/.config/birdoria/.env")
nim_api_key = None
with open(env_path) as f:
    for line in f:
        if line.startswith("GENAIPRO_API_KEY"):
            # Not needed for Nim
            pass

# Nim uses OAuth via MCP, can't call directly from script
# Instead, use the MCP tool via a different approach

# Actually, let's check if Nim has a REST API we can call directly
# Nim MCP is OAuth-based, no direct REST API available from here

print("ERROR: Nim requires OAuth via MCP connector, cannot call from Python script directly.")
print("Need to use MCP tools from Claude context.")
