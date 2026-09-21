<h1 align="center">🔄 batch-image-converter</h1>

<p align="center">
  <b>"Convert 200 images to WebP" shouldn't mean uploading 200 images to a stranger's server.</b><br>
  A whole folder converted and resized in one command — WebP, JPG, PNG, SVG, PSD. Nothing leaves your machine.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Photopea-powered-6E59F7" alt="Photopea">
  <img src="https://img.shields.io/badge/no%20upload-100%25%20local-1f9d55" alt="Local, no upload">
  <img src="https://img.shields.io/badge/Photoshop-not%20required-E1306C" alt="No Photoshop">
  <img src="https://img.shields.io/badge/API%20key-none-brightgreen" alt="No API key">
  <img src="https://img.shields.io/badge/license-MIT-yellow" alt="MIT">
</p>

**Claude Code:**

```
/plugin marketplace add mohamed-amine-ben-mallessa/batch-image-converter
/plugin install batch-image-converter
```

**Codex, Cursor, Copilot, Gemini CLI, or any of 50+ [Agent Skills](https://agentskills.io) hosts:**

```
npx skills add mohamed-amine-ben-mallessa/batch-image-converter -g
```

---

## Why this exists

Every "free online converter" is the same deal: your files go to someone's server, you get
ads, a size cap, a sign-up wall, and a paywalled batch mode.

Photopea decodes and encodes **inside your own browser sandbox** — your files never leave
your computer, and there's no native codec to install. This repo scripts that over an
entire folder.

| Online converters | **batch-image-converter** |
|---|---|
| 🚫 Upload your files to a server | ✅ **100% local** — nothing leaves your computer |
| One file at a time / paywalled batch | ✅ **Whole folder** in one command |
| Ads, size limits, sign-ups | ✅ **Free**, MIT, unlimited |
| Black-box quality | ✅ You set format, quality, size |
| Can't be called by your agent | ✅ **Is a skill** your agent already knows |

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

So it doubles as: **HEIC → JPG** (the iPhone photo problem), **PNG → WebP** (shrink a whole
site's assets), **any → PSD**, **raster → SVG-wrapped**, plus folder-wide **resize /
downscale**.

## Options

| Flag | Does |
|---|---|
| `--to {png,jpg,webp,psd,svg}` | output format (default `webp`) |
| `--quality N` | JPG quality 1-100 |
| `--max N` | cap the longest side to N px (keeps aspect ratio) |
| `--width N --height N` | resize to exact dimensions |
| `--recursive` | include subfolders |

## Install

| Surface | Install | Updates |
|---|---|---|
| **Claude Code** (recommended) | `/plugin marketplace add mohamed-amine-ben-mallessa/batch-image-converter` then `/plugin install batch-image-converter` | `claude plugin update batch-image-converter` |
| **Codex, Cursor, Copilot, Gemini CLI, or any of 50+ [Agent Skills](https://agentskills.io) hosts** | `npx skills add mohamed-amine-ben-mallessa/batch-image-converter -g` | `npx skills update batch-image-converter -g` |
| **Any MCP agent** | Point it at [`skills/batch-image-converter/SKILL.md`](skills/batch-image-converter/SKILL.md) | `git pull` |
| **Plain Python** (no agent) | `git clone https://github.com/mohamed-amine-ben-mallessa/batch-image-converter` then run `scripts/convert.py` | `git pull` |

**Requirements:** Node (for `npx`) and Python ≥ 3.8. No API key, no account, no Photoshop.

## How it works

It drives the free **[Photopea](https://www.photopea.com)** MCP server: open each file →
(resize) → export in the target format. Photopea does all the decoding and encoding in the
browser sandbox, so there's **no upload and no native codec to install**. Core loop:
[`scripts/convert.py`](scripts/convert.py).

## For AI agents

[`skills/batch-image-converter/SKILL.md`](skills/batch-image-converter/SKILL.md) lets an
agent run conversions on request — "convert this folder to webp under 1600px" — with the
exact tool args, no trial and error.

## The pack

| | Repo | One job |
|---|---|---|
| 🔄 | **batch-image-converter** (this) | A whole folder converted/resized, 100% locally |
| 🎨 | [photopea-as-code](https://github.com/mohamed-amine-ben-mallessa/photopea-as-code) | The driver, the recipes, the full scripting reference |
| 📱 | [social-post-factory](https://github.com/mohamed-amine-ben-mallessa/social-post-factory) | One brand theme → square, story, banner |
| 🖼️ | [bulk-mockups](https://github.com/mohamed-amine-ben-mallessa/bulk-mockups) | 1 PSD → hundreds of mockups via smart objects |

## Credits

Built on **[Photopea](https://www.photopea.com)** and
[photopea-mcp-server](https://github.com/attalla1/photopea-mcp-server). Independent toolkit,
not affiliated with Photopea or Adobe. Trademarks belong to their owners.

## License

MIT.

---

<p align="center">
  <sub>Built by <a href="https://github.com/mohamed-amine-ben-mallessa">Mohamed Amine Ben Mallessa</a> · ⭐ star it if it kept your files off someone else's server</sub>
</p>
