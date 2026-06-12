#!/usr/bin/env python3
"""
convert.py — batch-convert (and optionally resize) a folder of images with Photopea.

Everything runs locally in your browser via Photopea — your images are NOT uploaded
anywhere. Free, no Photoshop, no API key.

    # convert every image in ./in to WebP, written to ./out
    python convert.py ./in ./out --to webp

    # convert to JPG at quality 80 and cap the longest side to 1600px
    python convert.py ./in ./out --to jpg --quality 80 --max 1600

    # just resize PNGs to exactly 512x512 (keep format)
    python convert.py ./in ./out --to png --width 512 --height 512

Input formats Photopea reads: PNG, JPG, WebP, SVG, PSD, GIF, BMP, TIFF, HEIC, AVIF, RAW…
Output formats: png, jpg, webp, psd, svg.

The first conversion opens a browser window — that's Photopea, leave it open.
Node (for the Photopea MCP via npx) is the only prerequisite.
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from photopea import Photopea, PhotopeaError  # noqa: E402

READABLE = (".png", ".jpg", ".jpeg", ".webp", ".svg", ".psd", ".gif",
            ".bmp", ".tif", ".tiff", ".heic", ".heif", ".avif", ".ico")
OUT_FORMATS = ("png", "jpg", "webp", "psd", "svg")


def list_images(folder: str, recursive: bool) -> list[str]:
    out = []
    if recursive:
        for root, _dirs, files in os.walk(folder):
            for f in files:
                if f.lower().endswith(READABLE):
                    out.append(os.path.join(root, f))
    else:
        for f in os.listdir(folder):
            p = os.path.join(folder, f)
            if os.path.isfile(p) and f.lower().endswith(READABLE):
                out.append(p)
    return sorted(out)


def _doc_size(pp: Photopea) -> tuple[int, int]:
    import json
    res = pp.run_script(
        'app.echoToOE(JSON.stringify({w:app.activeDocument.width,h:app.activeDocument.height}));')
    try:
        d = json.loads(res)
        return int(d["w"]), int(d["h"])
    except Exception:  # noqa: BLE001
        return 0, 0


def convert_one(pp: Photopea, src: str, dst: str, fmt: str, quality, width, height, max_side):
    pp.call("photopea_open_file", {"source": os.path.abspath(src)})
    # resizing
    if width and height:
        pp.call("photopea_resize_document", {"width": int(width), "height": int(height)})
    elif max_side:
        w, h = _doc_size(pp)
        if w and h and max(w, h) > max_side:
            scale = max_side / float(max(w, h))
            pp.call("photopea_resize_document",
                    {"width": max(1, round(w * scale)), "height": max(1, round(h * scale))})
    # export
    args = {"outputPath": os.path.abspath(dst), "format": fmt}
    if fmt == "jpg" and quality is not None:
        args["quality"] = int(quality)
    pp.call("photopea_export_image", args)
    # free RAM, then close the doc so the next open is clean
    pp.run_script("app.activeDocument.clearHistory(); app.activeDocument.close(); app.echoToOE('ok');")


def main() -> int:
    ap = argparse.ArgumentParser(description="Batch image converter (Photopea, local, no upload).")
    ap.add_argument("input_dir")
    ap.add_argument("output_dir")
    ap.add_argument("--to", default="webp", choices=OUT_FORMATS, help="output format")
    ap.add_argument("--quality", type=int, default=None, help="JPG quality 1-100")
    ap.add_argument("--max", type=int, default=None, dest="max_side",
                    help="cap the longest side to N px (keeps aspect)")
    ap.add_argument("--width", type=int, default=None, help="exact width (with --height)")
    ap.add_argument("--height", type=int, default=None, help="exact height (with --width)")
    ap.add_argument("--recursive", action="store_true", help="recurse into subfolders")
    args = ap.parse_args()

    imgs = list_images(args.input_dir, args.recursive)
    if not imgs:
        print(f"no readable images in {args.input_dir}")
        return 1
    os.makedirs(args.output_dir, exist_ok=True)

    print(f"{len(imgs)} images → .{args.to}"
          + (f", max {args.max_side}px" if args.max_side else "")
          + (f", {args.width}x{args.height}" if args.width and args.height else ""))
    ok, fail = 0, 0
    with Photopea() as pp:
        for src in imgs:
            base = os.path.splitext(os.path.basename(src))[0]
            dst = os.path.join(args.output_dir, f"{base}.{args.to}")
            try:
                convert_one(pp, src, dst, args.to, args.quality, args.width, args.height, args.max_side)
                print(f"  ✓ {os.path.basename(src)} → {os.path.basename(dst)}")
                ok += 1
            except Exception as e:  # noqa: BLE001
                print(f"  ✗ {os.path.basename(src)}: {e}")
                fail += 1
    print(f"\ndone: {ok} ok, {fail} failed → {args.output_dir}")
    return 0 if fail == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
