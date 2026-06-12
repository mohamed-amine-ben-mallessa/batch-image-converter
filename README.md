<h1 align="center">🔄 batch-image-converter</h1>

<p align="center">
  <b>Convert and resize a whole folder of images — locally, in one command.</b><br>
  WebP, JPG, PNG, SVG, PSD. Nothing is uploaded. Free, no Photoshop, no API key.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Photopea-powered-6E59F7" alt="Photopea">
  <img src="https://img.shields.io/badge/no%20upload-100%25%20local-1f9d55" alt="Local, no upload">
  <img src="https://img.shields.io/badge/Photoshop-not%20required-E1306C" alt="No Photoshop">
  <img src="https://img.shields.io/badge/API%20key-none-brightgreen" alt="No API key">
  <img src="https://img.shields.io/badge/license-MIT-yellow" alt="MIT">
</p>

---

> **"Convert 200 images to WebP" usually means uploading 200 images to some random
> website.** This doesn't. Photopea runs the conversion in your own browser — your
> files never leave your machine — and this repo scripts it over an entire folder.

## Why this one's different

| Online converters | **batch-image-converter** |
|---|---|
| 🚫 Upload your files to a server | ✅ **100% local** — nothing leaves your computer |
| One file at a time / paywalled batch | ✅ **Whole folder** in one command |
| Ads, size limits, sign-ups | ✅ **Free**, MIT, unlimited |
| Black-box quality | ✅ You set format, quality, size |

## Quick start

```bash
# Node is the only prereq (the Photopea MCP is fetched via npx on first run).

# convert every image in ./in to WebP → ./out
python scripts/convert.py ./in ./out --to webp

# JPG at quality 80, cap the longest side at 1600px
python scripts/convert.py ./in ./out --to jpg --quality 80 --max 1600

# resize everything to exactly 512×512 PNG
python scripts/convert.py ./in ./out --to png --width 512 --height 512

# recurse into subfolders
python scripts/convert.py ./in ./out --to webp --recursive
```

The first conversion opens a browser window (that's Photopea — leave it open). Each image
is opened, optionally resized, and re-exported into `./out`.

## Formats

**Reads:** PNG · JPG · WebP · SVG · PSD · GIF · BMP · TIFF · HEIC/HEIF · AVIF · ICO · RAW…
(anything Photopea can open).
**Writes:** `png` · `jpg` · `webp` · `psd` · `svg`.

So it doubles as: **HEIC → JPG**, **PNG → WebP** (shrink for the web), **any → PSD**,
**raster → SVG-wrapped**, plus folder-wide **resize / downscale**.

## Options

| Flag | Does |
|---|---|
| `--to {png,jpg,webp,psd,svg}` | output format (default `webp`) |
| `--quality N` | JPG quality 1-100 |
| `--max N` | cap the longest side to N px (keeps aspect ratio) |
| `--width N --height N` | resize to exact dimensions |
| `--recursive` | include subfolders |

## How it works

It drives the free **[Photopea](https://www.photopea.com)** MCP server: open each file →
(resize) → export in the target format. Photopea does all the decoding/encoding in the
browser sandbox, so there's **no upload and no native codec to install**. Core loop:
[`scripts/convert.py`](scripts/convert.py).

## For AI agents

[`skills/batch-image-converter/SKILL.md`](skills/batch-image-converter/SKILL.md) lets an
agent run conversions on request ("convert this folder to webp under 1600px") with the
exact tool args, no trial and error.

## Related

- 🎨 **[photopea-as-code](https://github.com/mohamed-amine-ben-mallessa/photopea-as-code)** — the full Photopea-as-code toolkit + scripting reference.
- 🖼️ **[bulk-mockups](https://github.com/mohamed-amine-ben-mallessa/bulk-mockups)** — 1 PSD → N mockups.
- 📱 **[social-post-factory](https://github.com/mohamed-amine-ben-mallessa/social-post-factory)** — branded social posts in one command.

## Credits

Built on **[Photopea](https://www.photopea.com)** and
[photopea-mcp-server](https://github.com/attalla1/photopea-mcp-server). Independent toolkit,
not affiliated with Photopea or Adobe. Trademarks belong to their owners.

## License

MIT.
