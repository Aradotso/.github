# Branding asset guide

This directory is the working home for Ara brand assets used by designers and developers. Keep source files, generated exports, and implementation tokens close together so updates can be reviewed and shipped without guessing which logo, color, or type scale is current.

The current GitHub profile already uses these brand images one directory up:

- `../logo.png`: 512 × 512 PNG app/profile mark used for avatars, social previews, and compact placements.
- `../hero.png`: 1280 × 768 PNG hero image used at the top of the profile README.

As the brand library grows, place new canonical assets in this `branding/` directory and keep the profile-level files as published exports that are generated from, or copied from, the canonical sources documented here.

## Recommended directory contents

Use this structure for new or refreshed brand assets:

```text
branding/
  README.md
  logos/
    ara-logo.svg
    ara-logo-dark.svg
    ara-logo-light.svg
    ara-logo-512.png
    ara-logo-256.png
    ara-logo-128.png
    ara-logo-64.png
  heroes/
    github-profile-hero.png
    social-card.png
  colors/
    tokens.json
    tokens.css
  typography/
    scale.md
    scale.json
  sources/
    figma.md
    brand-system.md
```

## What belongs here

Logos should include SVG masters plus exported PNG sizes for surfaces that cannot use SVG. SVG files are the source of truth for shape, color, spacing, and accessibility metadata. PNG files are generated artifacts for GitHub, app stores, social platforms, favicons, and integrations that require raster images.

Hero and social images should include the dimensions in the filename or source notes. Keep each exported image tied to a specific use case, such as GitHub profile hero, Open Graph card, launch announcement image, or product screenshot frame.

Color tokens should define the canonical palette in machine-readable formats. Prefer a `tokens.json` source plus generated `tokens.css` custom properties. Include semantic names such as `brand.background`, `brand.foreground`, `brand.accent`, `surface.card`, and `text.muted` rather than only raw color names.

Typography files should document the production type scale: font family, fallback stack, font weights, line heights, tracking, and responsive sizes. If a design tool owns the source of truth, link it in `sources/` and export implementation-ready values here.

Source notes should link to upstream design files, decision records, or product docs. Add a short note when a source is unavailable so future contributors know whether an asset was manually created, exported from Figma, or copied from another repository.

## Which asset to use

Use SVG logos for web UI, documentation pages, presentations, and any surface that supports vector artwork. SVG preserves crisp edges at any size and should be the default for product and marketing work.

Use PNG logos for GitHub profile images, social avatars, app integrations, email clients, favicons, and any tool that rejects SVG. Match the PNG size to the requested display size and avoid scaling a small PNG up.

Use the 512px logo for high-resolution avatars, profile images, and source exports. Use 256px or 128px exports for integrations that ask for smaller square icons. Use 64px only for compact UI or favicon-style placements.

Use dark or light logo variants only when the default mark does not meet contrast requirements on the target background. Do not recolor a logo ad hoc in a consuming app; add a reviewed variant here instead.

Use hero images only for the named surface they were created for. The current `../hero.png` is sized for the GitHub profile README and should not be reused as a generic social card unless it is explicitly validated at the required crop and safe area.

Use color tokens in code instead of copying hex values from an image or design mock. If a one-off color is needed for a prototype, add it to the token draft first and promote it after review.

## Adding a new logo variant

Start from the SVG master, not from a PNG export. Create the new SVG under `branding/logos/` with a descriptive name such as `ara-logo-dark.svg`, `ara-logo-mono.svg`, or `ara-logo-horizontal.svg`.

Keep the viewBox stable across variants when possible so consumers can swap files without layout shifts. Preserve accessible metadata such as `<title>` or `aria-label` when present. Check that the mark has adequate clear space and meets contrast requirements on its intended background.

Generate PNG exports from the SVG at the required sizes. Recommended square exports are 512, 256, 128, and 64 pixels. Name them consistently, for example `ara-logo-dark-512.png`.

Update this README with the new variant, when to use it, and any restrictions. If the variant replaces an older file, note the migration path and keep the old file only when active consumers still need it.

## Adding a new color

Add new colors to the source token file first, usually `branding/colors/tokens.json`. Use semantic names that describe purpose rather than appearance. For example, prefer `brand.accent` over `pink500` unless the token is truly a raw palette step.

Include the color value, intended usage, and contrast notes. When adding foreground/background pairs, verify they meet the required WCAG contrast target for the text size and context.

Regenerate implementation outputs such as `tokens.css` after editing the source token file. Update consuming apps to import the token instead of hard-coding the value.

Avoid deleting or renaming existing tokens without checking downstream usage. If a token must be replaced, add the new token, migrate consumers, then remove the deprecated token in a separate cleanup.

## Tools and validation

Use ImageMagick for quick raster resizing when a source SVG or high-resolution PNG is available:

```bash
magick branding/logos/ara-logo.svg -resize 512x512 branding/logos/ara-logo-512.png
magick branding/logos/ara-logo.svg -resize 256x256 branding/logos/ara-logo-256.png
magick branding/logos/ara-logo.svg -resize 128x128 branding/logos/ara-logo-128.png
magick branding/logos/ara-logo.svg -resize 64x64 branding/logos/ara-logo-64.png
```

Use `svgo` to optimize SVG files after export, while preserving IDs, titles, and viewBox values that consuming code or accessibility tools depend on:

```bash
npx svgo branding/logos/ara-logo.svg --pretty
```

Use `file` or `sips` on macOS to confirm generated dimensions before committing:

```bash
file branding/logos/ara-logo-512.png
sips -g pixelWidth -g pixelHeight branding/logos/ara-logo-512.png
```

For color changes, validate JSON token syntax and inspect generated CSS before shipping:

```bash
python -m json.tool branding/colors/tokens.json >/dev/null
```

There is no dedicated asset generation script in this repository yet. If generation becomes repeatable, add a script such as `scripts/generate-brand-assets.sh`, document its inputs and outputs here, and make it safe to run from a clean checkout.

## Upstream sources

Primary public site: https://www.ara.so

GitHub profile repository: https://github.com/Aradotso/.github

No Figma file, formal brand book, or upstream design document is currently linked in this repository. When one exists, add it under `branding/sources/figma.md` or `branding/sources/brand-system.md` with the owner, last-reviewed date, and export instructions.

## Review checklist

Before committing brand asset changes, confirm that filenames are descriptive, generated dimensions are correct, SVGs are optimized without breaking accessibility metadata, color tokens pass syntax checks, and every new asset has a documented use case in this guide.

If a profile-level asset such as `../logo.png` or `../hero.png` changes, preview `../README.md` to confirm the image still renders well in GitHub's light and dark themes.
