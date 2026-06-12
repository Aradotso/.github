# Branding assets

This directory is the home for Ara brand source files and generated exports. Use it as the shared reference for designers preparing brand updates and developers wiring those assets into websites, apps, documentation, release notes, and social previews.

At the moment, this worktree only includes the public profile assets in `../profile/`: `logo.png` is a 512×512 transparent PNG suitable for avatars and app-style icons, and `hero.png` is a 1280×768 RGB hero/banner image used by `../profile/README.md`. Treat those files as the current upstream assets until SVG masters, token files, and generated sizes are added here.

## What belongs in `branding/`

Expected structure:

```text
branding/
  README.md                 This guide.
  logos/                    Source logos and generated logo exports.
    ara-logo.svg            Editable SVG master for the primary mark.
    ara-logo-dark.svg       Dark-background variant, if needed.
    ara-logo-light.svg      Light-background variant, if needed.
    png/                    Generated PNG exports by size.
      ara-logo-32.png
      ara-logo-64.png
      ara-logo-128.png
      ara-logo-256.png
      ara-logo-512.png
  colors/                   Brand color tokens for design and code.
    tokens.json             Canonical color names and values.
    tokens.css              CSS custom properties generated from tokens.
  typography/               Type scale and font usage guidance.
    scale.json              Font sizes, line heights, weights, and roles.
  figma/                    Export notes, source links, or snapshots.
```

Keep editable source files next to the generated assets they produce. Generated exports should be deterministic and replaceable from the source SVGs or token files.

## How to use each asset

Use SVG masters for product UI, marketing sites, decks, and any placement where the mark can remain vector-based. Prefer SVG because it scales cleanly, keeps file sizes small, and allows accessibility metadata to stay with the artwork.

Use PNG exports when the destination does not accept SVG, such as app stores, social profile images, favicon fallbacks, email clients, or third-party directories. Choose the smallest PNG that is at least as large as the rendered display size. For example, use a 512×512 export for profile avatars and a 32×32 or 64×64 export for favicon fallbacks.

Use color tokens instead of hard-coded hex values in product code. `colors/tokens.json` should be the canonical cross-platform source. Generated files like `tokens.css` should be derived from it and checked in only when they are consumed directly by apps or docs.

Use the typography scale for headings, body text, labels, captions, and marketing display text. Developers should map product styles to the named roles in `typography/scale.json` rather than inventing one-off font sizes.

When using `../profile/logo.png`, preserve the transparent background, do not crop inside the mark, and render it at square dimensions. When using `../profile/hero.png`, preserve the original aspect ratio unless a target platform explicitly requires a crop.

## Adding a new logo variant

1. Add or update the editable SVG master under `branding/logos/`.
2. Name variants by purpose and background, for example `ara-logo-dark.svg`, `ara-logo-light.svg`, `ara-logomark.svg`, or `ara-wordmark.svg`.
3. Export PNGs into `branding/logos/png/` using predictable size suffixes such as `-32`, `-64`, `-128`, `-256`, and `-512`.
4. Optimize SVGs before committing them. Keep IDs, metadata, and embedded raster images only when they are required.
5. Update this README with usage notes if the new variant has constraints, such as “only use on dark backgrounds” or “minimum width 120 px”.
6. Replace downstream references only after verifying the new asset renders correctly in the consuming app or document.

Do not overwrite an existing logo variant with a materially different design unless it is intended to become the canonical replacement. If both versions are still valid, add a new variant with a more specific name.

## Adding a new color

1. Add the color to `branding/colors/tokens.json` with a semantic name, not just a visual name. Prefer names like `backgroundPrimary`, `accentFlight`, or `textMuted` over `pink500` unless the palette is explicitly scale-based.
2. Include the hex value and, when useful, the intended contrast role or usage note.
3. Regenerate derived outputs such as `branding/colors/tokens.css`.
4. Check contrast for text and UI states before using the color in production.
5. Update any design-system documentation that references the palette.

Avoid adding duplicate colors with slightly different names. If a new value replaces an existing token, keep the semantic token name stable and change the value in one place.

## Generation and validation tools

Recommended tools for this repo:

```bash
# Optimize SVG masters before export.
npx svgo branding/logos/*.svg

# Export common PNG sizes from an SVG master.
magick branding/logos/ara-logo.svg -resize 32x32 branding/logos/png/ara-logo-32.png
magick branding/logos/ara-logo.svg -resize 64x64 branding/logos/png/ara-logo-64.png
magick branding/logos/ara-logo.svg -resize 128x128 branding/logos/png/ara-logo-128.png
magick branding/logos/ara-logo.svg -resize 256x256 branding/logos/png/ara-logo-256.png
magick branding/logos/ara-logo.svg -resize 512x512 branding/logos/png/ara-logo-512.png

# Inspect dimensions and color mode for generated PNGs.
file branding/logos/png/*.png
```

If the repo later adds package scripts, prefer wrapping these commands in scripts such as `pnpm brand:optimize`, `pnpm brand:resize`, and `pnpm brand:validate` so designers and developers can run the same workflow.

Validation checklist before committing brand assets:

- SVGs open in a browser and design tool without missing fonts or embedded broken links.
- PNGs have the expected dimensions and transparent backgrounds where required.
- Token files parse as valid JSON, CSS, or the relevant target format.
- New colors meet contrast requirements for their intended text or UI use.
- README usage notes match the files that are actually present.

## Upstream brand sources

Known public source in this worktree: `../profile/README.md`, which references `../profile/hero.png`, `../profile/logo.png`, and [ara.so](https://www.ara.so).

No Figma file, internal design doc, or canonical upstream brand repository is present in this worktree. When those sources exist, add links here with owner and update cadence, for example:

```text
Figma: <link to Ara brand file>
Design docs: <link to brand system or visual identity guide>
Source of truth owner: Design / Brand
Last reviewed: YYYY-MM-DD
```

Until a Figma or design-doc source is added, treat committed SVG masters and token files in `branding/` as the version-controlled source of truth, and treat `../profile/logo.png` and `../profile/hero.png` as the current published examples.