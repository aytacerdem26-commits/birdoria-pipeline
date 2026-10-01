#!/usr/bin/env python3
"""Render edilmis kareleri dogrular.

Bos (tek renk) kare = HATA, cikis 1. Videoya beyaz bosluk sizmasini engeller.
Yinelenen kare = UYARI, cikis 0. Bir sahneyi tutmak kasitli olabilir.

Bos kare kasitliysa (ornegin beyaza fade) ALLOW_BLANK=1 ile gecin.
"""
import hashlib
import os
import sys
from collections import defaultdict

from PIL import Image

# Bir rengin karenin bu oranindan fazlasini kaplamasi "neredeyse bos" sayilir.
NEAR_BLANK_RATIO = 0.995
# Dominantlik olcumu icin kucultulmus kopya (tam boyutta saymak yavas).
THUMB = (320, 180)


def analyze(path):
    """Kareyi incele: (tek_renk_mi, baskin_oran, baskin_renk, md5)."""
    with open(path, "rb") as fh:
        digest = hashlib.md5(fh.read()).hexdigest()

    im = Image.open(path).convert("RGB")
    # getextrema tam kesin ve hizli: her kanalda min==max ise tek renk.
    solid = all(lo == hi for lo, hi in im.getextrema())

    th = im.resize(THUMB, Image.NEAREST)
    colors = th.getcolors(maxcolors=THUMB[0] * THUMB[1])
    count, color = max(colors)
    ratio = count / (THUMB[0] * THUMB[1])

    return solid, ratio, color, digest


def main():
    frames_dir = sys.argv[1] if len(sys.argv) > 1 else "out/frames"
    allow_blank = os.environ.get("ALLOW_BLANK") == "1"

    names = sorted(f for f in os.listdir(frames_dir) if f.endswith(".png"))
    if not names:
        print(f"     HATA: {frames_dir} icinde PNG yok")
        return 1

    blank, near, by_hash = [], [], defaultdict(list)

    for name in names:
        solid, ratio, color, digest = analyze(os.path.join(frames_dir, name))
        by_hash[digest].append(name)
        if solid:
            blank.append((name, color))
        elif ratio >= NEAR_BLANK_RATIO:
            near.append((name, ratio, color))

    for name, color in blank:
        print(f"     {'UYARI' if allow_blank else 'HATA '}: {name} tek renk {color} — bos kare")
    for name, ratio, color in near:
        print(f"     UYARI: {name} %{ratio * 100:.1f} {color} — neredeyse bos")

    # Ardisik ikizler tutulan sahne olabilir; yine de gorunur olsun.
    for group in by_hash.values():
        if len(group) > 1:
            idx = [names.index(g) for g in group]
            kind = "ardisik" if idx == list(range(min(idx), max(idx) + 1)) else "daginik"
            print(f"     UYARI: ayni kare ({kind}) -> {', '.join(group)}")

    print(f"     {len(names)} kare | bos {len(blank)} | neredeyse bos {len(near)}")

    if blank and not allow_blank:
        print("     Bos kare kasitliysa ALLOW_BLANK=1 ./render.sh ile calistir.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
