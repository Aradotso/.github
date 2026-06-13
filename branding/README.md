# Branding

This folder is the canonical home for Ara brand assets that designers and developers can reference without digging through app-specific folders. If an asset is intended for reuse across websites, apps, decks, social profiles, or press kits, add it here before copying it elsewhere.

At the time this guide was added, the repository only contained GitHub profile artwork in `profile/hero.png` and `profile/logo.png`; no `branding/` assets had been checked in yet. Use the structure below when adding the first shared brand files.

## What belongs here

Recommended layout:

```text
branding/
  README.md
  logos/
    ara-logo.svg
    ara-logo-dark.svg
    ara-logo-light.svg
    ara-mark.svg
    png/
      ara-logo-256.png
      ara-logo-512.png
      ara-logo-1024.png
      ara-mark-256.png
      ara-mark-512.png
      ara-mark-1024.png
  colors/
    tokens.json
    tokens.css
  typography/
    scale.json
    scale.css
  source/
    figma.md
    originals/
```

Use `logos/` for production-ready logo files. Keep editable SVG masters at the top of `logos/`, and generated PNG exports under `logos/png/`.

Use `colors/` for brand color tokens that can be imported by code. Prefer a machine-readable `tokens.json` source plus generated CSS variables in `tokens.css`.

Use `typography/` for font-family choices, type scale, line heights, tracking, and role names such as `display`, `headline`, `body`, `caption`, and `mono`.

Use `source/` for upstream references such as Figma links, original exports, brand docs, naming notes, and any source files that should not be edited directly by product code.

## Which asset to use

Use SVG logos for websites, apps, docs, and any layout where the logo can be rendered as vector artwork. SVG should be the default for production UI because it scales cleanly and keeps file size low.

Use PNG logos when the destination does not support SVG, such as some social profiles, email clients, presentation templates, marketplace listings, or Open Graph images. Pick the smallest PNG that is at least 2x the displayed pixel size.

Use full wordmark variants when the audience may not already know Ara. Use mark-only variants for favicons, avatars, compact UI chrome, watermarks, or places where the wordmark would be too small to read.

Use dark/logo-on-light variants on white, cream, pale gray, or bright backgrounds. Use light/logo-on-dark variants on black, navy, saturated gradients, or image backgrounds with enough contrast. Do not add drop shadows, outlines, glows, skew, rotation, or recoloring unless the source brand file explicitly includes that treatment.

Use color tokens from `colors/` rather than hard-coded hex values in product code. Designers should name new colors by purpose, not appearance, when the color represents a product decision. For example, prefer `brand.background` or `accent.primary` over `pink-500` unless it is a raw palette step.

Use typography tokens from `typography/` for reusable UI roles. Product code should consume named roles rather than retyping font sizes and line heights in every component.

## Adding a logo variant

1. Start from the editable SVG master in `branding/logos/` or the upstream design source. Do not trace or screenshot an existing PNG.
2. Export the new variant as SVG with a descriptive lowercase kebab-case name, such as `ara-logo-light.svg`, `ara-mark-square.svg`, or `ara-logo-for-dark-bg.svg`.
3. Keep the SVG viewBox intact, remove editor metadata, and make sure the file does not include embedded raster images unless the brand source requires it.
4. Generate PNG exports only when a downstream surface needs them. Use 256, 512, and 1024 pixel exports for avatars and general-purpose reuse.
5. Add a short note in this README if the variant has a specific use case, background requirement, or do-not-use constraint.
6. Update any consumers that should switch to the new shared asset instead of keeping a duplicated app-local copy.

Suggested commands when local tools are available:

```bash
npx svgo branding/logos/ara-logo-light.svg
mkdir -p branding/logos/png
qlmanage -t -s 1024 -o branding/logos/png branding/logos/ara-logo-light.svg
sips -Z 512 branding/logos/png/ara-logo-light.png --out branding/logos/png/ara-logo-light-512.png
sips -Z 256 branding/logos/png/ara-logo-light.png --out branding/logos/png/ara-logo-light-256.png
```

If using a dedicated export script later, document it here and make the script deterministic so regenerated files produce stable diffs.

## Adding a color

1. Add the color to the source token file, preferably `branding/colors/tokens.json`.
2. Include the hex value, intended usage, and contrast guidance for text or icon use.
3. Regenerate any derived files such as CSS variables, Tailwind theme entries, Swift colors, or platform-specific token exports.
4. Replace one-off hard-coded values in product code with the token when the new color is intended for reuse.
5. Validate contrast before using the color for text, icons, focus rings, or status states.

Suggested token shape:

```json
{
  "brand": {
    "foreground": { "value": "#111111", "usage": "Primary text and logo on light backgrounds" },
    "background": { "value": "#FFFFFF", "usage": "Default light brand background" },
    "accent": { "value": "#FF4FD8", "usage": "Primary accent for highlights and calls to action" }
  }
}
```

## Generation and validation

Use SVG optimization for checked-in SVGs. `svgo` is the expected tool if no repo-specific script exists yet.

Use macOS `sips`, `qlmanage`, Figma export presets, or a checked-in script for PNG resizing. Generated PNGs should preserve transparency, avoid extra whitespace, and use predictable names that include size when multiple sizes exist.

Before committing brand assets, verify:

- SVGs open in a browser and have a valid `viewBox`.
- PNG exports are the expected pixel dimensions.
- Transparent assets do not include unintended background fills.
- Dark and light variants have enough contrast on their intended backgrounds.
- Token files are valid JSON or CSS.
- Generated files can be reproduced from documented sources.

Useful local checks:

```bash
npx svgo --multipass branding/logos/*.svg
sips -g pixelWidth -g pixelHeight branding/logos/png/*.png
python3 -m json.tool branding/colors/tokens.json >/dev/null
```

Only run commands that match files that exist in the checkout.

## Upstream sources

Known checked-in sources today:

- GitHub profile hero image: `profile/hero.png`
- GitHub profile logo image: `profile/logo.png`
- Public website: https://www.ara.so

No Figma URL, design-system document, or upstream brand-source link was present in this worktree when this README was created. When one exists, add it to `branding/source/figma.md` and link it from this section with the owner, last-reviewed date, and export instructions.

## Ownership notes

Designers should update the source design files first, then export optimized assets here. Developers should consume assets from this folder and avoid editing generated image files by hand. If a product needs a temporary asset, keep it app-local until it is approved as a reusable brand asset, then promote it into `branding/` with the relevant source and generation notes.
