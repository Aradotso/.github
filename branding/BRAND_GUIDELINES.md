# Ara Brand Guidelines

This document defines the core visual and typographic standards for the Ara brand. Consistency across all touchpoints — product UI, docs, marketing, open-source repos — reinforces trust and recognition.

---

## Logo

The Ara logo is a minimal wordmark / icon lockup. The master source is `../profile/logo.png` (512×512 PNG, RGBA). Pre-exported sizes live in `logos/`.

| File | Use case |
|------|----------|
| `logos/ara-logo-16x16.png` | Browser favicon, small icon slots |
| `logos/ara-logo-32x32.png` | App icons, toolbar icons |
| `logos/ara-logo-64x64.png` | Notification icons, list thumbnails |
| `logos/ara-logo-256x256.png` | macOS app bundle, marketing thumbnails |
| `logos/ara-logo-512x512.png` | App Store submissions, high-resolution print |

### Logo usage rules

- **Minimum clear space**: equal to the height of the "A" glyph on all sides.
- **Minimum size**: do not render the logo below 16×16 px.
- **Backgrounds**: the logo is white on dark by default. Use a dark (`#0D0D0D` or `#1A1A1A`) background. On light backgrounds, use the dark-mark variant (charcoal `#525252` on white).
- **Do not** recolor, rotate, stretch, add drop shadows, or place the logo on busy photographic backgrounds without an adequate contrast buffer.
- **Do not** combine the Ara logo with another company's logo in a way that implies partnership without written permission.

---

## Color Palette

### Primary

| Name | HEX | RGB | Usage |
|------|-----|-----|-------|
| Ara Black | `#0D0D0D` | `rgb(13, 13, 13)` | Primary background, hero sections |
| Ara White | `#FFFFFF` | `rgb(255, 255, 255)` | Logo mark, primary text on dark |
| Ara Charcoal | `#525252` | `rgb(82, 82, 82)` | Logo mark on light backgrounds, secondary UI elements |

### Secondary / Accent

| Name | HEX | RGB | Usage |
|------|-----|-----|-------|
| Cool Grey 100 | `#F5F5F5` | `rgb(245, 245, 245)` | Light-mode page background |
| Cool Grey 300 | `#D0D0D0` | `rgb(208, 208, 208)` | Dividers, subtle borders |
| Cool Grey 500 | `#909090` | `rgb(144, 144, 144)` | Disabled states, placeholder text |
| Slate Blue | `#8AAFC0` | `rgb(138, 175, 192)` | Hero image accent, link hover, highlights |
| Ara Ink | `#1A1A1A` | `rgb(26, 26, 26)` | Body text on light backgrounds |

### Semantic

| Name | HEX | Usage |
|------|-----|-------|
| Success | `#22C55E` | Confirmations, agent task complete |
| Warning | `#F59E0B` | Degraded states, caution notices |
| Error | `#EF4444` | Failures, destructive actions |
| Info | `#3B82F6` | Informational callouts |

---

## Typography

Ara uses a clean sans-serif system that prioritises legibility at small sizes and works well across platforms without custom font loading.

### Typefaces

| Role | Font | Fallback stack |
|------|------|----------------|
| UI / Product | [Geist Sans](https://vercel.com/font) | `"Geist Sans", "Inter", "SF Pro Text", system-ui, sans-serif` |
| Marketing headings | [Geist Sans](https://vercel.com/font) | same as above |
| Monospace / Code | [Geist Mono](https://vercel.com/font) | `"Geist Mono", "SF Mono", "Fira Code", monospace` |

### Type scale (base 16 px)

| Token | Size | Weight | Line height | Use |
|-------|------|--------|-------------|-----|
| `display-xl` | 56 px | 700 | 1.1 | Hero headlines |
| `display-lg` | 40 px | 700 | 1.15 | Section titles |
| `heading-md` | 28 px | 600 | 1.25 | Sub-section headings |
| `heading-sm` | 20 px | 600 | 1.3 | Card titles, modal headers |
| `body-lg` | 18 px | 400 | 1.6 | Long-form prose |
| `body-md` | 16 px | 400 | 1.6 | Default body text |
| `body-sm` | 14 px | 400 | 1.5 | Secondary text, captions |
| `label` | 12 px | 500 | 1.4 | Labels, badges, chips |
| `code` | 14 px | 400 | 1.5 | Inline and block code |

---

## Spacing & Layout

- Base unit: **4 px** (0.25 rem). All spacing values should be multiples of 4 px.
- Content max-width: **1280 px** for full-bleed layouts, **800 px** for prose/docs.
- Border radius: `4 px` (tight), `8 px` (default components), `16 px` (cards/panels), `9999 px` (pills/badges).

---

## Iconography

Ara uses [Lucide](https://lucide.dev) as the default icon library. Icon sizing follows the type scale base unit (16 px, 20 px, 24 px). Stroke weight: 1.5 px.

---

## Voice & Tone

- **Concise**: say the minimum necessary. No filler, no padded copy.
- **Action-oriented**: prefer verbs. "Build an agent" not "Get started with agent building".
- **Direct**: address the user as "you". Skip the passive voice.
- **Technical but approachable**: assume a developer audience; never talk down, never over-explain the basics.

---

## Questions / Updates

For brand questions or to request new asset exports, open an issue in this repository or contact the Ara design team at [sven@ara.so](mailto:sven@ara.so).
