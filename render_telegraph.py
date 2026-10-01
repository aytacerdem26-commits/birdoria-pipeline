import subprocess, os, json

FPS = 30
ROOT = "/Users/aytacerdem/zenn"
IMG = f"{ROOT}/telegraph_images"
STOCK = f"{ROOT}/telegraph_stock"
OUTDIR = f"{ROOT}/telegraph_render"
os.makedirs(OUTDIR, exist_ok=True)

rows = json.load(open(f"{ROOT}/telegraph_scenes.json"))

def kenburns_filter(preset, d_frames):
    target_zoom = 1.15
    rate = (target_zoom - 1.0) / max(d_frames, 1)
    if preset == "zoomin":
        z = f"min(zoom+{rate:.6f},{target_zoom})"
        x = "iw/2-(iw/zoom/2)"
        y = "ih/2-(ih/zoom/2)"
    elif preset == "zoomout":
        z = f"if(eq(on,0),{target_zoom},max(1.0,zoom-{rate:.6f}))"
        x = "iw/2-(iw/zoom/2)"
        y = "ih/2-(ih/zoom/2)"
    elif preset == "panleft":
        z = f"{target_zoom}"
        x = f"(iw-iw/zoom)*(1-on/{d_frames})"
        y = "ih/2-(ih/zoom/2)"
    elif preset == "panright":
        z = f"{target_zoom}"
        x = f"(iw-iw/zoom)*(on/{d_frames})"
        y = "ih/2-(ih/zoom/2)"
    return f"zoompan=z='{z}':x='{x}':y='{y}':d={d_frames}:s=1920x1080:fps={FPS}"

presets = ["zoomin", "zoomout", "panleft", "panright"]

for idx, r in enumerate(rows):
    num = r['num']
    dur = float(r['dur'].rstrip('s'))
    out = f"{OUTDIR}/clip_{num:03d}.mp4"
    if os.path.exists(out):
        continue
    img_path = f"{IMG}/scene_{num:02d}.jpg"
    stock_path = f"{STOCK}/scene_{num}.mp4"
    typ = "AI" if os.path.exists(img_path) else "STOCK"
    if typ == "AI":
        path = img_path
        preset = presets[num % 4]
        d_frames = int(round(dur * FPS))
        kb = kenburns_filter(preset, d_frames)
        vf = f"scale=5760:-2,{kb},setsar=1,format=yuv420p"
        cmd = [
            "ffmpeg", "-y", "-loop", "1", "-i", path,
            "-t", str(dur), "-r", str(FPS),
            "-vf", vf,
            "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", out,
            "-loglevel", "error",
        ]
    else:
        path = stock_path
        vf = "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,format=yuv420p"
        cmd = [
            "ffmpeg", "-y", "-stream_loop", "-1", "-i", path,
            "-t", str(dur),
            "-vf", vf,
            "-r", str(FPS),
            "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-an", out,
            "-loglevel", "error",
        ]
    print(f"[{idx+1}/{len(rows)}] rendering scene {num} kind={typ} dur={dur:.2f}")
    subprocess.run(cmd, check=True)

with open(f"{OUTDIR}/concat_list.txt", "w") as f:
    for r in rows:
        f.write(f"file '{OUTDIR}/clip_{r['num']:03d}.mp4'\n")

print("ALL SCENES RENDERED")
