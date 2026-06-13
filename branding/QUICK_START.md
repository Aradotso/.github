# Ara brand quick start

This guide gives teams the defaults for using Ara visuals consistently across GitHub profiles, ara.so surfaces, the desktop app, social posts, and small icons. It is grounded in the assets in this repo plus the current `ara-cua` / `ara.so` design tokens.

## Logo usage

Use the logo in its original proportions and give it room to breathe. Minimum clear space is one quarter of the rendered logo width on every side.

| Context | Use | Asset / treatment | Notes |
| --- | --- | --- | --- |
| Website / landing page | Full-width brand hero or product visual | `profile/hero.png` for large GitHub/profile hero placements; ara.so site logo treatment uses `/logo/colors/black.png` with `--color-logo-filter` and `--ara-logo-invert` | Use on light or dark backgrounds with the theme-aware filter. Do not crop the hero unless the target is explicitly a cover image. |
| App / product chrome | Monochrome Ara mark or wordmark matched to the current theme | ara.so tokens invert the logo with `--ara-logo-invert`; app/marketing colors mirror `AraColors.swift` comments in `AraWeb/ara.so/src/pages/ara.css` | Prefer native system-rendered contrast: black mark on light surfaces, white mark on dark surfaces. |
| Social / open graph | Hero-style brand image with enough negative space for safe cropping | `profile/hero.png` at 1280 × 768 | Keep key content inside the center 80% safe area so previews can crop to 1.91:1, 16:9, or square. |
| Small icon / favicon / avatar | Square icon mark | `profile/logo.png` at 512 × 512; chat surfaces also reference `/brand/favicon.ico`, `/brand/favicon-32x32.png`, `/brand/favicon-16x16.png`, and `/brand/apple-touch-icon.png` | Use the square mark for anything below 64px, app icons, GitHub org avatars, browser icons, and notification badges. |

Do not redraw, recolor, rotate, distort, add gradients, add drop shadows, place the mark inside a new container shape, or use low-resolution screenshots of the logo.

## Primary color palette

Use the ara.so marketing/app palette first. The default product feel is neutral, system-native, and high contrast rather than saturated brand color. Use semantic colors only for state.

| Role | CSS variable | Hex | RGB |
| --- | --- | --- | --- |
| Light background | `--ara-bg`, `--ara-dither-bg` | `#f7f7f7` | `rgb(247, 247, 247)` |
| Light elevated background | `--ara-bg-elevated`, `--color-surface` | `#ffffff` | `rgb(255, 255, 255)` |
| Light alternate background | `--color-bg-alt`, `--color-secondary` | `#f5f5f5` | `rgb(245, 245, 245)` |
| Sidebar background | `--color-sidebar` | `#fafafa` | `rgb(250, 250, 250)` |
| Light border | `--ara-border`, `--color-border` | `#e7e5e4` | `rgb(231, 229, 228)` |
| Light border hover | `--color-border-hover` | `#d6d3d1` | `rgb(214, 211, 209)` |
| Light primary text / CTA | `--ara-text`, `--ara-cta-bg` | `#111111` | `rgb(17, 17, 17)` |
| Product text | `--color-text`, `--color-accent` | `#1c1917` | `rgb(28, 25, 23)` |
| Secondary text | `--color-text-secondary`, `--color-text-muted` | `#78716c` | `rgb(120, 113, 108)` |
| Tertiary text | `--color-text-tertiary`, `--color-text-subtle` | `#a8a29e` | `rgb(168, 162, 158)` |
| Dark background | `--ara-bg`, `--ara-dither-bg` in dark mode | `#141414` | `rgb(20, 20, 20)` |
| Dark elevated background | `--ara-bg-elevated` in dark mode | `#1f1e1d` | `rgb(31, 30, 29)` |
| Dark border | `--ara-border` in dark mode | `#2f2d2b` | `rgb(47, 45, 43)` |
| Dark primary text / CTA | `--ara-text`, `--ara-cta-bg` in dark mode | `#ffffff` | `rgb(255, 255, 255)` |
| Success | `--color-success` | `#16a34a` | `rgb(22, 163, 74)` |
| Error | `--color-error` | `#FF3535` | `rgb(255, 53, 53)` |
| Warning | `--color-warning` | `#f59e0b` | `rgb(245, 158, 11)` |

`chat.ara.so` currently has a darker chat-local token set: `--bg: #0a0a0a`, `--fg: #ededed`, `--muted: #888`, `--border: #222`, and `--accent: #3b82f6`. Treat that as chat-surface UI chrome, not the canonical marketing palette.

## Typography scale

Ara uses system typography so the product feels native on macOS and the web. The canonical family is `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`, exposed in ara.so as `--font-sans`, `--font-serif`, and `--font-mono` for now. Body and title weights default to `--font-body-weight: 400` and `--font-title-weight: 400`; use `600` sparingly for logos, labels, and emphasized UI.

| Token / use | Size | Line-height | Weight | Source |
| --- | --- | --- | --- | --- |
| Hero H1 | `clamp(40px, 5vw, 72px)` | `1.08` | `400` | `.ara-site .ara-hero-h1` |
| Site logo text | `18px` | `1` or normal | `600` | `.ara-site .ara-logo` |
| Nav links | `14px` | `1` | `400` | `.ara-site .ara-nav-link` |
| API/simple product pages | `15px` | `1.5` | `400` | Embedded checkout / gateway pages |
| Utility UI | `14px` | `1.4` | `400` | Session recording viewer |
| Section/card display copy | Tailwind `text-3xl` to `text-5xl` | tight | `900` only for campaign pages | `chat.ara.so` experimental pages |
| Code or tabular UI | System sans for now | match body | `400` | `--font-mono` is currently aliased to system sans |

Keep tracking tight on large display type (`letter-spacing: -0.03em` for hero copy and `-0.02em` for compact logo text). Avoid importing a separate webfont unless the design tokens are updated first.

## Spacing and grid

Use a 4px base unit and compose layout spacing in 8px increments. This matches existing code patterns such as 4px radii, 8px gaps, 12px side padding, 20px compact nav padding, 24px page padding, 32px cards, 40px mobile-safe gutters, and 48px desktop nav gutters.

| Rule | Default |
| --- | --- |
| Base spacing unit | 4px |
| Micro gaps | 4px / 8px |
| Form and list item padding | 8px to 12px |
| Card padding | 24px to 32px |
| Page gutters | 24px mobile, 40px tablet, 48px+ desktop |
| Desktop nav height | 52px at top, 44px when scrolled |
| Nav max width when scrolled | `min(700px, calc(100vw - 40px))` |
| Hero/content max width | 1280px layout shell, 640px text column |
| Dot-grid texture | 16px × 16px background grid |
| Border radius | 4px for nav chrome, 6px to 8px for controls, 14px to 32px for cards/modals |

Prefer generous negative space. Keep product UI aligned to simple columns, avoid dense decorative grids, and let the neutral background/dither texture carry the brand feel.

## Dos and don'ts

Do:

- Use `profile/logo.png` for small square placements and `profile/hero.png` for large brand/profile placements.
- Use the ara.so variables (`--ara-*` and bridged `--color-*`) instead of hard-coded one-off colors when building web surfaces.
- Keep logo contrast theme-aware with black-on-light and white-on-dark treatments.
- Keep typography system-native and light-weight by default.
- Preserve clear space around the mark and keep the logo crisp at export size.
- Use semantic state colors only for success, warning, and error states.

Don't:

- Stretch, skew, rotate, crop, outline, or recreate the logo.
- Add unapproved gradients, shadows, glows, stickers, or container shapes to the mark.
- Use the chat-local blue accent as the main Ara brand color outside chat UI.
- Mix multiple font families or add webfont dependencies without updating the shared tokens.
- Put text or important UI outside social preview safe areas.
- Reduce contrast below accessible UI contrast, especially on muted text and glass surfaces.

## Shared design resources

No shared Figma file or Storybook instance was found in this checkout or in the local `ara-cua` search results. If one is added later, link it here and make it the canonical source for exported logo variants and component examples.

Current source references:

- `profile/logo.png`
- `profile/hero.png`
- `AraWeb/ara.so/src/index.css` in `ara-cua`
- `AraWeb/ara.so/src/pages/ara.css` in `ara-cua`
- `chat.ara.so/app/globals.css` in `ara-cua`
- `chat.ara.so/app/layout.tsx` in `ara-cua`
