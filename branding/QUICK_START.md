# Ara brand quick start

This guide captures the practical brand rules for the Ara GitHub profile and public ara.so surfaces. It is grounded in the assets currently in this repo and the live ara.so CSS tokens.

## Logo usage

Use `profile/logo.png` as the default Ara mark. It is a 512 × 512 square asset with a white field and dark mark, so it works best on light surfaces or inside an explicit white app-icon tile.

Use `profile/hero.png` for wide website, GitHub profile, README, launch, and social banner contexts. It is a 1280 × 768 hero asset and should not be cropped into a square icon unless a designer exports a dedicated version.

Use the following variants by context:

| Context | Use | Notes |
| --- | --- | --- |
| Website header/nav | `profile/logo.png` mark, rendered at 24–40 px tall | On dark themes, invert the logo treatment with `--ara-logo-invert: 1` or use a dedicated light export if one is added. |
| Website hero/README | `profile/hero.png` | Keep the full composition visible. Do not crop off the browser/device frame. |
| App icon | `profile/logo.png` in a rounded square tile | Preserve the white field; use the native platform radius. Export sizes from the 512 px source. |
| Social avatar | `profile/logo.png` | Center the mark with safe padding so circular crops do not clip the edges. |
| Social banner/Open Graph | `profile/hero.png` or a composed banner using the same palette | Prefer a light neutral background and high-contrast text. |
| Small icon/favicon | `profile/logo.png`, simplified if legibility drops below 24 px | At 16 px, prefer a manually hinted favicon export over a direct downscale if one exists. |

Minimum clear space around the mark is one quarter of the rendered logo width. Do not place the logo on busy photography, saturated gradients, or low-contrast textures.

## Primary color palette

Use the `--ara-*` variables where CSS is available. Values below match the public ara.so light and dark themes.

### Light theme

| Role | CSS variable | Hex | RGB |
| --- | --- | --- | --- |
| Background | `--ara-bg` | `#f7f7f7` | `247, 247, 247` |
| Elevated surface | `--ara-bg-elevated` | `#ffffff` | `255, 255, 255` |
| Navigation background | `--ara-bg-nav` | `rgba(247, 247, 247, .72)` | `247, 247, 247, 0.72` |
| Primary text / primary CTA | `--ara-text`, `--ara-cta-bg` | `#111111` | `17, 17, 17` |
| Body text | `--ara-text-body` | `rgba(17, 17, 17, .7)` | `17, 17, 17, 0.7` |
| Muted text | `--ara-text-muted` | `rgba(17, 17, 17, .9)` | `17, 17, 17, 0.9` |
| Dim text | `--ara-text-dim` | `rgba(17, 17, 17, .8)` | `17, 17, 17, 0.8` |
| Faint text | `--ara-text-faint` | `rgba(17, 17, 17, .5)` | `17, 17, 17, 0.5` |
| Extra-faint text | `--ara-text-extra-faint` | `rgba(17, 17, 17, .4)` | `17, 17, 17, 0.4` |
| Border | `--ara-border` | `#e7e5e4` | `231, 229, 228` |
| Surface tint | `--ara-surface` | `rgba(0, 0, 0, .05)` | `0, 0, 0, 0.05` |
| Surface hover | `--ara-surface-hover` | `rgba(0, 0, 0, .03)` | `0, 0, 0, 0.03` |
| Card tint | `--ara-surface-card` | `rgba(0, 0, 0, .02)` | `0, 0, 0, 0.02` |
| CTA text | `--ara-cta-text` | `#ffffff` | `255, 255, 255` |
| Dither background | `--ara-dither-bg` | `#f7f7f7` | `247, 247, 247` |
| Dither foreground | `--ara-dither-fg` | `120, 120, 120` | `120, 120, 120` |

### Dark theme

| Role | CSS variable | Hex | RGB |
| --- | --- | --- | --- |
| Background | `--ara-bg` | `#141414` | `20, 20, 20` |
| Elevated surface | `--ara-bg-elevated` | `#1f1e1d` | `31, 30, 29` |
| Navigation background | `--ara-bg-nav` | `rgba(20, 20, 20, .72)` | `20, 20, 20, 0.72` |
| Primary text / primary CTA text | `--ara-text`, `--ara-cta-bg` | `#ffffff` | `255, 255, 255` |
| Body text | `--ara-text-body` | `rgba(255, 255, 255, .7)` | `255, 255, 255, 0.7` |
| Muted text | `--ara-text-muted` | `rgba(255, 255, 255, .9)` | `255, 255, 255, 0.9` |
| Dim text | `--ara-text-dim` | `rgba(255, 255, 255, .8)` | `255, 255, 255, 0.8` |
| Faint text | `--ara-text-faint` | `rgba(255, 255, 255, .5)` | `255, 255, 255, 0.5` |
| Extra-faint text | `--ara-text-extra-faint` | `rgba(255, 255, 255, .4)` | `255, 255, 255, 0.4` |
| Border | `--ara-border` | `#2f2d2b` | `47, 45, 43` |
| Surface tint | `--ara-surface` | `rgba(255, 255, 255, .06)` | `255, 255, 255, 0.06` |
| Surface hover | `--ara-surface-hover` | `rgba(255, 255, 255, .1)` | `255, 255, 255, 0.1` |
| Card tint | `--ara-surface-card` | `rgba(255, 255, 255, .04)` | `255, 255, 255, 0.04` |
| CTA text | `--ara-cta-text` | `#111111` | `17, 17, 17` |
| Dither background | `--ara-dither-bg` | `#141414` | `20, 20, 20` |
| Dither foreground | `--ara-dither-fg` | `255, 255, 255` | `255, 255, 255` |

Use `#ff3b00` (`255, 59, 0`) only as a sparing system/accent color where it already appears in product UI. It is not the core brand background.

## Typography scale

Ara web surfaces use the system sans stack: `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`. Product surfaces may expose this as `var(--font-sans)`; use that variable when present and fall back to the same stack.

| Role | Family | Size | Line-height | Tracking | Token/class match |
| --- | --- | --- | --- | --- | --- |
| Display / hero | System sans / `var(--font-sans)` | 48–96 px | 0.95–1.0 | Tight to normal | Use for landing page hero statements. |
| Page H1 | System sans / `var(--font-sans)` | 48–72 px | 1.0–1.05 | Tight to normal | Mirrors large responsive ara.so headings. |
| Section H2 | System sans / `var(--font-sans)` | 30–48 px | 1.08 | Normal | Matches `text-3xl sm:text-4xl lg:text-5xl leading-[1.08]`. |
| H3 / card title | System sans / `var(--font-sans)` | 20–24 px | 1.2–1.3 | Normal | Use for feature cards and grouped content. |
| Body large | System sans / `var(--font-sans)` | 18 px | 1.6–1.7 | Normal | Matches `sm:text-lg leading-relaxed`. |
| Body | System sans / `var(--font-sans)` | 16 px | 1.6–1.7 | Normal | Matches `text-base leading-relaxed`. |
| Small / metadata | System sans / `var(--font-sans)` | 14 px | 1.4–1.5 | Normal | Use with `--ara-text-faint` or `--ara-text-extra-faint`. |
| Caption / legal | System sans / `var(--font-sans)` | 12 px | 1.35–1.45 | Normal | Keep contrast high enough for accessibility. |

Keep headings plain and confident. Avoid decorative display fonts, novelty type, all-caps paragraphs, or heavy letter spacing.

## Spacing and grid

Build layouts on a 4 px base grid. Prefer Tailwind-compatible spacing values: 4, 8, 12, 16, 24, 32, 48, 64, 80, 96, and 128 px.

Use these practical rules:

| Area | Rule |
| --- | --- |
| Page max width | Use 1120–1280 px max content width for marketing pages. |
| Page gutters | Use 24 px mobile gutters, 32 px tablet gutters, and 48–64 px desktop gutters. |
| Section padding | Use 64–96 px vertical padding on desktop, 40–64 px on mobile. |
| Card padding | Use 20–32 px depending on density. |
| Grid columns | Use 1 column on mobile, 2 columns on tablet, 3–4 columns on desktop for feature cards. |
| Logo clear space | Keep at least 25% of the logo width clear on all sides. |
| Radius | Use rounded cards and icon tiles, but avoid pill-shaped everything. |
| Shadows | Use `--ara-shadow` for elevated hero/card moments; keep routine UI flatter. |

## Dos and don'ts

Do:

- Use the CSS variables above instead of hard-coded one-off neutrals.
- Keep the brand mostly monochrome, warm-neutral, and high contrast.
- Use `profile/logo.png` for square marks and `profile/hero.png` for wide placements.
- Preserve logo proportions and clear space.
- Keep copy direct, product-led, and plain-spoken.
- Test light and dark theme contrast before shipping.

Don't:

- Stretch, rotate, outline, recolor, or add effects to the logo.
- Put the mark on noisy imagery or low-contrast gradients.
- Use `profile/hero.png` as a favicon or small app icon.
- Introduce new accent colors without adding token names and accessibility checks.
- Mix in decorative fonts or inconsistent type scales.
- Crowd layouts; leave enough breathing room around cards, CTAs, and screenshots.

## Shared design references

No shared Figma file or Storybook URL is present in this profile repo. If one is added later, link it here and keep this quick start in sync with the canonical design tokens.
