# Ara brand quick start

Use this guide for lightweight Ara brand decisions in the GitHub profile, website surfaces, app UI, social images, and small icons. It is grounded in the current local assets in `profile/` plus the public `ara.so` CSS token bundle checked during this update.

## Logo and image variants

Use `profile/logo.png` for compact brand marks. It is a 512×512 RGBA PNG, so it works best anywhere a square icon or transparent mark is needed.

Use `profile/hero.png` for wide brand moments. It is a 1280×768 RGB PNG, so it works best as a profile hero, social preview, or large editorial header.

Use the website wordmark/lockup from `ara.so` for marketing pages when a full navigation or landing-page context already exists. If the implementation needs a static repo asset, use `profile/hero.png` as the fallback and keep the image centered.

Use `profile/logo.png` in app chrome, desktop icons, favicons, small social avatars, and GitHub org/profile images. Render it at 16, 24, 32, 48, 120, 256, or 512 px depending on the surface, and keep the source square.

Use `profile/hero.png` for social cards, Open Graph previews, launch posts, profile README headers, and large website hero cards. Crop from the center; avoid stretching it into very wide banners without a safe crop review.

For very small icons under 24 px, prefer the 512×512 logo PNG and do not add extra detail, text, outlines, or shadows.

## Primary color palette

The public `ara.so` bundle maps generic color names to semantic Ara tokens. Prefer semantic variables over raw hex values in product UI.

Light theme basics:

| Role | CSS variable | Hex / RGB |
| --- | --- | --- |
| Page background | `--ara-bg` | `#f7f7f7` / `rgb(247, 247, 247)` |
| Elevated background | `--ara-bg-elevated` | `#ffffff` / `rgb(255, 255, 255)` |
| Primary text | `--ara-text` | `#111111` / `rgb(17, 17, 17)` |
| Body text | `--ara-text-body` | `rgba(17, 17, 17, .7)` |
| Faint text | `--ara-text-faint` | `rgba(17, 17, 17, .5)` |
| Border | `--ara-border` | `#e7e5e4` / `rgb(231, 229, 228)` |
| Surface | `--ara-surface` | `rgba(0, 0, 0, .05)` |
| Card surface | `--ara-surface-card` | `rgba(0, 0, 0, .02)` |
| Primary CTA background | `--ara-cta-bg` | `#111111` / `rgb(17, 17, 17)` |
| Primary CTA text | `--ara-cta-text` | `#ffffff` / `rgb(255, 255, 255)` |

Dark theme basics:

| Role | CSS variable | Hex / RGB |
| --- | --- | --- |
| Page background | `--ara-bg` | `#141414` / `rgb(20, 20, 20)` |
| Elevated background | `--ara-bg-elevated` | `#1f1e1d` / `rgb(31, 30, 29)` |
| Primary text | `--ara-text` | `#ffffff` / `rgb(255, 255, 255)` |
| Body text | `--ara-text-body` | `rgba(255, 255, 255, .7)` |
| Faint text | `--ara-text-faint` | `rgba(255, 255, 255, .5)` |
| Border | `--ara-border` | `#2f2d2b` / `rgb(47, 45, 43)` |
| Surface | `--ara-surface` | `rgba(255, 255, 255, .06)` |
| Card surface | `--ara-surface-card` | `rgba(255, 255, 255, .04)` |
| Primary CTA background | `--ara-cta-bg` | `#ffffff` / `rgb(255, 255, 255)` |
| Primary CTA text | `--ara-cta-text` | `#111111` / `rgb(17, 17, 17)` |

Compatibility aliases from `ara.so` include `--color-bg`, `--color-surface`, `--color-border`, `--color-text`, `--color-text-secondary`, `--color-accent`, and `--color-accent-foreground`. Keep new UI on the `--ara-*` names when possible.

## Typography scale

Use the same system-first stack found in `ara.so` tokens: `system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif`. The site currently maps both `--font-sans` and `--font-mono` to this stack, so avoid introducing a custom display font without updating tokens.

| Use | Token | Size | Line-height | Notes |
| --- | --- | --- | --- | --- |
| Caption / metadata | `--text-xs` | `0.75rem` / 12 px | `calc(1 / .75)` | Use sparingly for labels and timestamps. |
| Small UI | `--text-sm` | `0.875rem` / 14 px | `calc(1.25 / .875)` | Default for compact buttons and secondary nav. |
| Body | `--text-base` | `1rem` / 16 px | `1.5` | Default prose and form copy. |
| Large body | `--text-lg` | `1.125rem` / 18 px | `calc(1.75 / 1.125)` | Intro copy and roomy UI content. |
| Lead | `--text-xl` | `1.25rem` / 20 px | `calc(1.75 / 1.25)` | Short page leads and card headlines. |
| Section heading | `--text-2xl` | `1.5rem` / 24 px | `calc(2 / 1.5)` | Dense headings. |
| Page heading | `--text-3xl` | `1.875rem` / 30 px | `1.2` | Standard page titles. |
| Marketing heading | `--text-4xl` | `2.25rem` / 36 px | `calc(2.5 / 2.25)` | Landing page sections. |
| Hero heading | `--text-5xl` | `3rem` / 48 px | `1` | Use with tight tracking. |
| Large hero | `--text-8xl` | `6rem` / 96 px | `1` | Only for high-impact marketing moments. |

Use `--tracking-tight` (`-.025em`) for large headings, `--tracking-wide` (`.025em`) for small uppercase labels, and `--leading-relaxed` (`1.625`) for long-form prose.

## Spacing and grid rules

Use the `ara.so` spacing base token `--spacing: .25rem`, equivalent to a 4 px grid. Build spacing as multiples of that token: 1 = 4 px, 2 = 8 px, 3 = 12 px, 4 = 16 px, 6 = 24 px, 8 = 32 px, 10 = 40 px, 12 = 48 px, 14 = 56 px, and 16 = 64 px.

Keep standard content inside container tokens where possible: `--container-sm` 24 rem, `--container-md` 28 rem, `--container-lg` 32 rem, `--container-2xl` 42 rem, `--container-3xl` 48 rem, `--container-4xl` 56 rem, and `--container-5xl` 64 rem. The current marketing CSS also uses wide containers up to about 1520 px for immersive sections.

Use 16 px mobile gutters, 24 px tablet gutters, and 32 px desktop gutters. Use 12-column layouts for marketing pages, one or two columns for app UI, and centered max-width prose for documentation.

Use radius tokens for UI surfaces: `--radius-md` `.375rem` / 6 px, `--radius-lg` `.5rem` / 8 px, `--radius-xl` `.75rem` / 12 px, `--radius-2xl` `1rem` / 16 px, and `--radius-3xl` `1.5rem` / 24 px. Use `9999px` only for pills, avatars, and circular controls.

## Dos

- Use `profile/logo.png` for square marks and small icons.
- Use `profile/hero.png` for large social/profile/header treatments.
- Use semantic `--ara-*` color variables instead of hard-coded one-off colors.
- Keep contrast high by pairing `--ara-cta-bg` with `--ara-cta-text`.
- Keep layouts on the 4 px spacing grid.
- Use tight tracking for large headings and relaxed line-height for long prose.
- Crop brand imagery from the center and preserve the original aspect ratio.

## Don'ts

- Do not recolor, skew, stretch, rotate, or outline the logo.
- Do not place the logo on busy backgrounds without enough contrast.
- Do not use screenshots as source logo artwork when `profile/logo.png` is available.
- Do not mix unrelated accent palettes into core brand UI.
- Do not introduce a custom font family unless the shared tokens are updated too.
- Do not compress social cards so tightly that the logo or hero image becomes illegible.
- Do not create new spacing values when a 4 px grid multiple works.

## Shared design sources

No shared Figma file, Storybook instance, local token package, or source design file is referenced in this repository. A bounded check found no repo-visible Figma or Storybook link; `storybook.ara.so` returned 404, and `https://ara.so/storybook` rendered the normal site shell rather than Storybook. If a private Figma or Storybook exists, add its reviewed link here and keep this guide as the public quick start.
