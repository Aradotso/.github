# Ara Branding Quick Start

Use this guide when creating Ara visuals for GitHub, ara.so, product UI, launch graphics, and partner/social placements. It is grounded in the current GitHub profile assets plus the live ara.so/AraDesktop tokens.

## Assets and source of truth

- GitHub profile assets in this repo: `profile/logo.png` and `profile/hero.png`.
- Public brand kit: [ara.so/ara-brand-kit.zip](https://www.ara.so/ara-brand-kit.zip).
- Product/site token references: `AraWeb/ara.so/src/index.css`, `AraWeb/ara.so/src/pages/ara.css`, and AraDesktop color tokens mirrored by the ara.so marketing CSS.
- Shared Figma: none found in this repo or the referenced ara-cua/ara.so sources.
- Storybook: none found in this repo or the referenced ara-cua/ara.so sources.

## Logo variants

| Context | Use | Notes |
| --- | --- | --- |
| Website header / landing pages | `logo/ara-logo-color.png` from the brand kit on light backgrounds; `logo/ara-logo-white.png` on dark or photographic backgrounds | Default to the colored mark when the canvas is clean and light. Switch to white or black for contrast, not CSS filters. |
| App chrome / product UI | Monochrome mark, usually `logo/ara-logo-black.png` in light mode and `logo/ara-logo-white.png` in dark mode | Keep product UI quiet. The mark should feel like navigation, not decoration. |
| Social avatar / small icon | `profile/logo.png`, `logo/ara-icon.png`, or app icon exports such as `ara-icon-512.png` where available | Use square icon artwork for anything below 64px or inside a circular crop. Avoid the full wordmark at small sizes. |
| Social header / Open Graph image | `profile/hero.png` or custom artwork based on the brand kit | Keep large, calm whitespace. Make the Ara mark legible at thumbnail size. |
| Launch or themed graphics | `logo/colors/{pink,blue,orange,green}.png` from the brand kit | Use accent variants sparingly for campaigns, playlists, demos, or playful moments. Do not use them as permanent product identity. |
| Busy or photographic background | `logo/ara-logo-white.png` or `logo/ara-logo-black.png` | Pick the version with the clearest contrast and add empty space behind it rather than shadows or outlines. |

Minimum clear space: keep at least one logo-height of empty space around the mark on every side. Scale source PNGs down, never up.

## Primary color palette

Use ara.so marketing tokens for brand surfaces and app tokens for product UI. The marketing page bridges its Ara tokens into the shared `--color-*` variables, so designers and engineers can use either naming layer when appropriate.

| Role | CSS variable | Hex / RGB | Usage |
| --- | --- | --- | --- |
| Light background | `--ara-bg`, bridged to `--color-bg` | `#f7f7f7` / `rgb(247, 247, 247)` | Marketing canvas and system-aware Ara surfaces. |
| Light elevated background | `--ara-bg-elevated` | `#ffffff` / `rgb(255, 255, 255)` | Cards, sheets, nav elevation, and pure-white brand-kit canvases. |
| Light primary text / CTA | `--ara-text`, `--ara-cta-bg` | `#111111` / `rgb(17, 17, 17)` | Main copy, logo treatment, and primary button background in light mode. |
| Light border | `--ara-border`, bridged to `--color-border` | `#e7e5e4` / `rgb(231, 229, 228)` | Hairlines, cards, dividers. |
| Dark background | `--ara-bg` in dark mode | `#141414` / `rgb(20, 20, 20)` | Dark marketing and app canvas. |
| Dark elevated background | `--ara-bg-elevated` | `#1f1e1d` / `rgb(31, 30, 29)` | Raised dark surfaces. |
| Dark primary text / CTA | `--ara-text`, `--ara-cta-bg` in dark mode | `#ffffff` / `rgb(255, 255, 255)` | Main copy and inverted CTA background. |
| Dark border | `--ara-border` in dark mode | `#2f2d2b` / `rgb(47, 45, 43)` | Dark-mode hairlines and card edges. |
| Product text | `--color-text` | `#1c1917` / `rgb(28, 25, 23)` | Default app text when using the shared Tailwind theme. |
| Product secondary text | `--color-text-secondary`, `--color-text-muted` | `#78716c` / `rgb(120, 113, 108)` | Body metadata, helper text, subdued labels. |
| Product tertiary text | `--color-text-tertiary`, `--color-text-subtle` | `#a8a29e` / `rgb(168, 162, 158)` | Captions, placeholders, low-emphasis UI. |
| Product surface | `--color-bg-alt`, `--color-secondary` | `#f5f5f5` / `rgb(245, 245, 245)` | Subtle panels and secondary controls. |
| Success | `--color-success` | `#16a34a` / `rgb(22, 163, 74)` | Confirmation states only. |
| Error | `--color-error` | `#FF3535` / `rgb(255, 53, 53)` | Destructive or failed states only. |
| Warning | `--color-warning` | `#f59e0b` / `rgb(245, 158, 11)` | Attention states only. |

Opacity tokens used by ara.so: `--ara-text-body` is 70% text, `--ara-text-faint` is 50%, `--ara-surface` is a 5-6% fill, and `--ara-surface-hover` is the next hover step. Keep accent color as a guest, not the host.

## Typography scale

The active ara.so/product tokens use system UI everywhere: `--font-sans: system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif`. Use regular weight by default. The downloadable brand kit also describes a more editorial pairing, `"EB Garamond", ui-serif, Georgia, "Times New Roman", serif` for big brand headlines and `Inter, system-ui, -apple-system, sans-serif` for body; only use that pairing when those fonts are intentionally loaded in the surface you are designing.

| Token / class | Family | Size | Line-height | Weight | Use |
| --- | --- | --- | --- | --- | --- |
| `--font-sans` / site default | `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif` | Inherit | Inherit | 400 | App UI, marketing body, forms, buttons, and default headings. |
| `.ara-hero-h1` | Same as site default | `clamp(40px, 5vw, 72px)` | `1.08` | 400 | Main landing-page headline. Keep letter-spacing near `-0.03em`. |
| `.ara-h2` | Same as site default | `32px` | `1.2` | 400 | Section headings. Keep letter-spacing near `-0.02em`. |
| `.ara-h3` | Same as site default | `24px` | `1.3` | 400 | Feature/card headings. Keep letter-spacing near `-0.02em`. |
| `.ara-body` | Same as site default | `18px` | `1.6` | 400 | Longform marketing copy and feature descriptions. |
| `.ara-body-sm` | Same as site default | `14px` | `1.5` | 400 | Secondary copy, metadata, smaller UI notes. |
| `.ara-caption` | Same as site default | `12px` | Match context | 400 | Labels and eyebrow text; uppercase with `0.1em` letter-spacing. |
| `.ara-nav-link` | Same as site default | `14px` | `1` | 400 | Navigation links. |
| `.ara-logo` text fallback | Same as site default | `18px` | Match context | 600 | Text fallback only when an image logo cannot be used. |

Avoid bold typography in brand work. Create hierarchy through size, whitespace, contrast, and placement before adding weight.

## Spacing and grid rules

| Rule | Value | Source / use |
| --- | --- | --- |
| Base spacing rhythm | 4px increments, with 12px, 20px, 24px, 28px, and 48px appearing in ara.so components | Use the 4px grid for UI and docs so components snap cleanly. |
| Marketing max width | `1280px` | Hero and page sections should feel wide but composed. |
| Hero text width | `640px` | Keep headline measures short and calm. |
| Top nav height | `52px` default, `44px` scrolled | Match ara.so nav proportions. |
| Top nav horizontal padding | `48px` default, `20px` scrolled | Preserve airy launch-page framing. |
| Scrolled nav width | `min(700px, calc(100vw - 40px))` | Use compact glass navigation after scroll. |
| Dot-grid texture | `16px 16px` background-size | If adding brand texture, keep it subtle and low-contrast. |
| Card padding | `28px` | Default for larger brand/product cards. |
| Card radius | 6-10px for most UI, 24px for large feature panels, `9999px` for pills | ara.so intentionally reduced generic roundness; keep corners restrained. |
| Button padding | `12px 24px` for nav/download CTAs, `14px 28px` for hero CTAs | Use pill buttons for primary calls to action. |
| Badge/provider gap | `12px` | Useful for logo clouds and compact rows. |
| Provider badge min-height | `56px` | Keep partner/integration marks readable. |

Favor asymmetric editorial layouts, generous whitespace, and a quiet canvas. If a composition feels crowded, remove elements before shrinking type or tightening spacing.

## Do

- Use the real logo assets and choose the variant by contrast and size.
- Keep the brand restrained: white or near-white canvas, black ink, warm neutral borders, and very selective accents.
- Match ara.so tokens when designing website or product-adjacent surfaces.
- Use regular-weight typography and create drama with scale and whitespace.
- Keep screenshots and product frames crisp, quiet, and free of unnecessary chrome.
- Test logos at the final rendered size, especially social avatars and favicons.
- Use the public brand kit when handing assets to partners.

## Don't

- Do not recolor logo PNGs with CSS filters, hue rotation, shadows, strokes, glows, or gradients.
- Do not stretch, rotate, crop, or rebuild the mark.
- Do not place the colored logo on noisy backgrounds where it loses contrast.
- Do not make large fields of accent colors; accents are for moments, not the canvas.
- Do not mix in extra typefaces unless the design explicitly calls for loaded brand-kit typography.
- Do not use bold text as the default hierarchy mechanism.
- Do not invent new color tokens when an existing `--ara-*` or `--color-*` token fits.
- Do not ship a design that only works in light mode if it appears inside a system-aware product surface.
