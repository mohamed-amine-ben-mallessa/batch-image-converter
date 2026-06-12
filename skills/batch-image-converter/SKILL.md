---
name: batch-image-converter
description: >
  Convert and resize a whole folder of images locally with Photopea (free, no Photoshop,
  no upload). Use when the user wants to batch-convert images (e.g. HEIC to JPG, PNG to
  WebP, any to PSD), bulk-resize/downscale a folder, compress images for the web, or
  change image formats at scale without uploading files anywhere. Keywords: convert
  images, batch convert, bulk resize, webp, heic to jpg, png to webp, compress images,
  downscale, image format, no upload, photopea.
license: MIT
---

# batch-image-converter

Convert/resize a folder of images via the **photopea MCP** (free browser Photoshop).
Photopea decodes/encodes in the browser, so **nothing is uploaded** — good for private
files. The first tool call opens a browser window (expected).

## Per-image workflow
1. `photopea_open_file({source: "/abs/path/img.heic"})` — reads PNG/JPG/WebP/SVG/PSD/GIF/
   BMP/TIFF/HEIC/AVIF/RAW…
2. (optional resize) `photopea_resize_document({width, height})`. For "longest side ≤ N",
   read size first: `run_script('app.echoToOE(JSON.stringify({w:app.activeDocument.width,
   h:app.activeDocument.height}));')`, compute scale, then resize.
3. `photopea_export_image({outputPath:"/abs/out/img.webp", format:"webp"})` — writes
   png/jpg/webp/psd/svg. `quality` 1-100 applies to JPG only.
4. `run_script('app.activeDocument.clearHistory(); app.activeDocument.close(); app.echoToOE("ok");')`
   — free RAM and close before the next file.
5. Loop over the folder.

## Common jobs
- **HEIC → JPG**: open .heic → export jpg (quality ~85).
- **PNG → WebP** (web shrink): open .png → export webp.
- **Downscale a folder**: resize so longest side ≤ 1600 → export same/target format.
- **Anything → PSD / SVG-wrapped**: export psd / svg.

## Gotchas
- `open_file` arg is `source` (URL or absolute local path); `export_image` uses
  `outputPath` + `format`.
- Use absolute paths. Close the doc between files to keep memory flat for big batches.
- SVG output wraps the raster; true vectorization is `Image > Vectorize Bitmap` (separate).

A ready CLI runner with `--to/--quality/--max/--width/--height/--recursive` is in
`scripts/convert.py`.
