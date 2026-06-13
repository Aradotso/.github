# Branding assets

This folder is the canonical home for Ara brand assets that designers and developers can use in product surfaces, GitHub profile content, marketing pages, and launch materials. Today the repository ships the public GitHub profile assets in `../profile/`: `logo.png` is a 512 x 512 transparent PNG app/logo mark, and `hero.png` is a 1280 x 768 RGB hero image. Add new canonical assets here first, then copy or reference exported files from consuming folders such as `profile/`.

## Contents of `branding/`

Use this structure as the source-of-truth layout as the brand library grows:

```text
branding/
  README.md                 # Usage guide and contribution process
  logos/
    ara-mark.svg            # Editable SVG master for the symbol/app mark
    ara-wordmark.svg        # Editable SVG master for full wordmark lockups
    png/                    # Generated PNG exports at fixed sizes
      ara-mark-64.png
      ara-mark-128.png
      ara-mark-512.png
  colors.json               # Brand color tokens for code and design handoff
  typography.json           # Type scale, weights, and line-height tokens
  sources.md                # Links to Figma, design docs, and upstream sources
```

Keep editable masters, token files, and source links in `branding/`. Keep generated copies in the app, docs, or profile folder that consumes them only when that surface cannot reference `branding/` directly.

## Choosing the right asset

Use SVG masters for product UI, web pages, design handoff, and any surface where the logo may scale. SVGs stay crisp, are easier to theme, and should be the default for new implementation work.

Use PNG exports for GitHub READMEs, social cards, email clients, and other places that either block SVGs or need a fixed raster image. Prefer transparent PNGs for marks and logo lockups; use RGB PNGs or JPEGs only for photographic or full-bleed hero art.

Use the mark-only logo for app icons, favicons, avatars, small badges, and square placements. Use the wordmark for headers, landing pages, decks, and partner placements where the Ara name needs to be read. Do not stretch, recolor, crop, add shadows, or place the logo on low-contrast backgrounds unless a matching approved variant exists.

Use light variants on dark backgrounds and dark variants on light backgrounds. If both variants are unavailable, add the missing variant here before shipping a custom override in a downstream app.

Use color tokens from `colors.json` when implementing UI or documentation styles. Do not hard-code one-off hex values in product code if the color is meant to represent the Ara brand. Add a token first, then reference it from CSS variables, Tailwind config, Swift assets, or design tokens.

Use typography tokens from `typography.json` for reusable text styles such as display, heading, body, caption, and label. Product-specific layout can adapt spacing, but font family, weight, line height, and scale should start from the shared token names.

## Adding a logo variant

Start from the editable SVG master exported from Figma or the approved upstream source. Save it under `branding/logos/` with a descriptive lowercase name, for example `ara-mark-dark.svg` or `ara-wordmark-light.svg`.

Optimize the SVG before committing:

```sh
npx svgo branding/logos/ara-mark-dark.svg
```

Export PNG sizes only when a consuming surface needs raster files. Common sizes are 64, 128, 256, 512, and 1024 pixels for square marks. On macOS, `sips` can create predictable PNG exports from a high-resolution source:

```sh
mkdir -p branding/logos/png
sips -z 512 512 branding/logos/png/ara-mark-1024.png --out branding/logos/png/ara-mark-512.png
```

After exporting, preview the asset on both light and dark backgrounds, verify transparent padding is intentional, and update any consuming documentation such as `profile/README.md` if the new asset replaces an older copy.

## Adding a color token

Add colors to `branding/colors.json` using semantic names, not only visual names. Prefer `brand.primary`, `brand.accent`, `surface.dark`, or `text.inverse` over names like `pink1` when the token has a design role.

Each token should include a hex value, a short usage note, and any required contrast guidance. Example:

```json
{
  "brand.primary": {
    "hex": "#FF4FD8",
    "usage": "Primary Ara brand accent for links, highlights, and key calls to action.",
    "contrast": "Use on dark surfaces or with approved accessible pairings."
  }
}
```

Validate JSON before committing:

```sh
python3 -m json.tool branding/colors.json >/dev/null
```

If a token is generated into app-specific formats, regenerate those outputs in the same change and mention the affected apps in the PR description.

## Generation and validation tools

Use `svgo` for SVG cleanup, `sips` for simple macOS raster resizing, and `qlmanage -p` or the Finder preview pane for visual spot checks. For more advanced image pipelines, use a checked-in script so exports are reproducible instead of relying on one-off design-tool settings.

Before committing asset updates, run the lightest relevant checks:

```sh
npx svgo --version
python3 -m json.tool branding/colors.json >/dev/null
python3 -m json.tool branding/typography.json >/dev/null
```

Only run commands for files that exist in the change. Documentation-only updates should still pass `git diff --check`.

## Upstream brand sources

No Figma file, design-system document, or upstream brand-source URL is currently checked into this repository. When those sources are available, add them to `branding/sources.md` with owner, last-reviewed date, and access notes. Until then, treat `../profile/logo.png` and `../profile/hero.png` as the current public assets and avoid inventing new logo shapes or colors without design approval.

Known public destinations:

- Website: https://www.ara.so
- GitHub profile README assets: `../profile/logo.png` and `../profile/hero.png`

## Review checklist

Before merging a branding change, confirm that the new asset has a clear use case, SVG masters are optimized, generated PNG sizes are intentional, color and typography tokens validate, public profile copies are updated if needed, and source links are documented when they exist.
