# Branding asset guide

This directory is the home for reusable Ara brand assets. Use it as the source of truth for logos, color tokens, typography decisions, and generated exports that need to be shared across product, marketing, documentation, and GitHub profile surfaces.

The current repository stores the public GitHub profile artwork in `../profile/`: `logo.png` is a 512 × 512 RGBA icon suitable for avatars and square placements, and `hero.png` is a 1280 × 768 RGB hero image suitable for wide profile or landing-page placements. Until generated exports are checked into `branding/`, treat those profile assets as the active upstream raster exports and mirror any new canonical brand assets here.

## Contents

Expected files in `branding/`:

- `README.md`: this guide.
- `logos/`: finished logo exports organized by format and size.
  - `logos/svg/`: SVG masters and editable vector exports. These should be the canonical source for shape changes.
  - `logos/png/`: raster exports for apps, social previews, GitHub, docs, and places that cannot consume SVG.
  - `logos/icon/`: square app icons, favicons, and avatar-safe crops.
- `colors/`: machine-readable color tokens, usually JSON, CSS, or design-token files.
- `typography/`: typography scale, font pairing notes, and platform-specific type tokens.
- `figma/` or `sources/`: links, exports, and notes that point back to Figma, design docs, or upstream brand files.
- `scripts/`: generation and validation helpers for resizing PNGs, optimizing SVGs, checking color contrast, and validating filenames.

If a category is not present yet, create it when adding the first asset of that type. Keep source files and generated exports separate so designers can update masters without breaking developer references.

## When to use each asset

Use SVG masters when the environment supports vector graphics, especially websites, docs, pitch materials, and any placement that may be resized. Prefer SVG for crisp edges, small file size, and theme-aware variants.

Use PNG exports when the target system requires raster images, such as app stores, social cards, GitHub organization/profile images, email clients, and third-party integrations. Choose the smallest size that renders cleanly at the target display size. Use `@2x` or `@3x` exports for high-density displays.

Use square icon exports for avatars, favicons, app icons, launchers, and integrations that crop images into circles. Check that the mark has enough safe area around the edges before uploading to a service that applies automatic masking.

Use hero or wide-format artwork for README headers, launch announcements, blog posts, and landing-page sections. Do not crop wide artwork into square placements unless there is an approved square variant.

Use color tokens in code instead of manually copying hex values from screenshots or Figma. Product surfaces should consume token files where possible so theme updates can happen in one place.

Use typography tokens for headings, body copy, captions, and UI labels. Designers should update the scale at the source; developers should avoid one-off font sizes unless a component has a documented exception.

## How to add a logo variant

1. Start from the SVG master in `logos/svg/` or the approved upstream design source. Do not trace or recreate the logo from a raster screenshot.
2. Name the variant by usage, theme, and format, for example `ara-logo-primary-light.svg`, `ara-logo-mark-dark.svg`, or `ara-icon-512.png`.
3. Export required raster sizes into `logos/png/` or `logos/icon/`. Include dimensions in filenames for fixed-size exports, such as `ara-icon-512.png`.
4. Preserve transparent backgrounds for logos and icons unless the variant is intentionally backed by a brand color.
5. Optimize SVGs before committing and resize PNGs from the master, not from another PNG export.
6. Update this README with the new variant, intended usage, and any caveats.
7. If the asset replaces an existing file, verify every code or documentation reference that imports the old filename.

## How to add a color

1. Confirm the color in Figma or the upstream brand source before adding it.
2. Add the token to the canonical token file in `colors/` using a semantic name, such as `brand.primary`, `brand.accent`, `surface.canvas`, or `text.muted`.
3. Include values needed by consuming platforms, typically hex for design/docs, CSS variables for web, and any platform-specific exports used by apps.
4. Document intended usage, contrast expectations, and pairing rules. For example, note whether a color is only for decorative accents or can be used behind text.
5. Run contrast checks for text/background combinations before using the token in UI.
6. Update downstream generated files or scripts if the token pipeline is automated.

## Generation and validation tools

Use repeatable tools so committed assets can be regenerated:

- Image resizing: use ImageMagick (`magick input.png -resize 512x512 output.png`) or `sips` on macOS for deterministic raster exports.
- SVG optimization: use SVGO (`npx svgo logos/svg/*.svg`) before committing vector exports.
- PNG compression: use `pngquant`, `oxipng`, or an equivalent lossless/lossy optimizer appropriate for the asset.
- Metadata checks: use `file`, `identify`, or `sips -g pixelWidth -g pixelHeight` to confirm dimensions and color mode.
- Contrast checks: use a design-token pipeline, Storybook accessibility checks, or a WCAG contrast tool before approving text colors.

When adding scripts, place them under `branding/scripts/`, document required dependencies at the top of the script or in a local README, and make scripts safe to rerun without overwriting source masters unexpectedly.

## Upstream sources and links

Known public source in this repository:

- `../profile/logo.png`: current GitHub/profile square logo export, 512 × 512.
- `../profile/hero.png`: current GitHub/profile hero artwork, 1280 × 768.
- `../profile/README.md`: current consumer of the public profile assets.

No Figma file, internal design doc, or external upstream brand URL is currently checked into this repository. When those sources are available, add links here with owner, access notes, and the date the assets were last synced.

## Review checklist

Before merging a new or changed brand asset:

- The file has a clear, usage-based name.
- SVG masters are optimized and remain editable.
- Raster exports are generated from the master source at the required dimensions.
- Transparent, light, dark, and monochrome variants are present when needed.
- Color additions use semantic tokens and include contrast guidance.
- Typography updates include designer and developer usage notes.
- This guide and any consuming references are updated.
