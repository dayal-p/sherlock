#!/usr/bin/env python3
"""Cut an image into an NxN grid of overlapping, upscaled tiles for close inspection.

Usage: python3 tile_image.py IMAGE [--grid 3] [--scale 2] [--overlap 0.1] [--out tiles/]
Writes tile_r{row}_c{col}.png plus a contrast-enhanced copy of the full frame and prints EXIF if present.
"""
import argparse, os, sys
from PIL import Image, ImageOps, ImageEnhance


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("image")
    ap.add_argument("--grid", type=int, default=3)
    ap.add_argument("--scale", type=float, default=2.0)
    ap.add_argument("--overlap", type=float, default=0.1)
    ap.add_argument("--out", default="tiles")
    a = ap.parse_args()

    img = Image.open(a.image)
    exif = {}
    try:
        exif = {k: str(v)[:80] for k, v in (img.getexif() or {}).items()}
    except Exception:
        pass
    img = ImageOps.exif_transpose(img).convert("RGB")
    w, h = img.size
    os.makedirs(a.out, exist_ok=True)
    print(f"size={w}x{h} grid={a.grid} scale={a.scale}")
    if exif:
        print("exif tags (id: value):", exif)
    else:
        print("exif: none (stripped or screenshot)")

    tw, th = w / a.grid, h / a.grid
    ox, oy = tw * a.overlap, th * a.overlap
    for r in range(a.grid):
        for c in range(a.grid):
            box = (max(0, int(c * tw - ox)), max(0, int(r * th - oy)),
                   min(w, int((c + 1) * tw + ox)), min(h, int((r + 1) * th + oy)))
            tile = img.crop(box)
            tile = tile.resize((int(tile.width * a.scale), int(tile.height * a.scale)), Image.LANCZOS)
            p = os.path.join(a.out, f"tile_r{r+1}_c{c+1}.png")
            tile.save(p)
            print(p, box)
    enh = ImageEnhance.Contrast(ImageOps.autocontrast(img, cutoff=1)).enhance(1.2)
    enh.save(os.path.join(a.out, "full_enhanced.png"))
    print(os.path.join(a.out, "full_enhanced.png"))


if __name__ == "__main__":
    sys.exit(main())
