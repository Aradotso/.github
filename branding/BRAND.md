# Ara Brand Guidelines

This document captures the core visual identity for Ara — colors, typography, logo usage, and do/don'ts. It is the single source of truth for anyone building on or representing the Ara brand.

---

## Logo

The Ara logo is located in `branding/logos/`. Use the size closest to your target context.

| File | Size | Use case |
|---|---|---|
| `ara-logo-16.png` | 16 × 16 | Favicons, tiny badges |
| `ara-logo-32.png` | 32 × 32 | Browser tabs, small icons |
| `ara-logo-64.png` | 64 × 64 | App icons, README badges |
| `ara-logo-256.png` | 256 × 256 | Marketing, print, hi-DPI screens |
| `ara-logo-512.png` | 512 × 512 | Master — use as source for derivative work |

### Logo usage rules

- **Do** maintain the original aspect ratio (1 : 1 square).
- **Do** use the logo on white, near-white, or dark backgrounds with sufficient contrast.
- **Don't** recolor, stretch, rotate, or add drop shadows to the logo.
- **Don't** place the logo on a busy photographic background without a clear-space buffer equal to at least half the logo's width.
- **Don't** combine the Ara logo mark with another company's logo without prior written approval.

---

## Colors

### Primary palette

| Name | HEX | RGB | Usage |
|---|---|---|---|
| Ara Pink | `#FF2D87` | `255, 45, 135` | Primary CTA buttons, highlights, links on dark backgrounds |
| Ara Dark | `#0A0A0F` | `10, 10, 15` | Page backgrounds, nav bars |
| Ara White | `#FAFAFA` | `250, 250, 250` | Body text on dark, card backgrounds |

### Secondary palette

| Name | HEX | RGB | Usage |
|---|---|---|---|
| Ara Lavender | `#C084FC` | `192, 132, 252` | Accent gradients, secondary highlights |
| Ara Slate | `#1E1E2E` | `30, 30, 46` | Card surfaces, code blocks |
| Ara Muted | `#6B7280` | `107, 114, 128` | Body copy, subtitles |

### Semantic tokens

| Token | Value | Meaning |
|---|---|---|
| `--color-brand` | `#FF2D87` | Brand primary |
| `--color-bg` | `#0A0A0F` | Default page background |
| `--color-surface` | `#1E1E2E` | Elevated surface |
| `--color-text` | `#FAFAFA` | Default text |
| `--color-text-muted` | `#6B7280` | Secondary text |
| `--color-accent` | `#C084FC` | Accent / gradient end |

---

## Typography

### Typefaces

| Role | Family | Weight | Notes |
|---|---|---|---|
| Display / Headings | **Inter** | 700 (Bold) | Used for H1–H3, hero text |
| Body | **Inter** | 400 (Regular) | Paragraphs, UI labels |
| Monospace / Code | **JetBrains Mono** | 400 | Code snippets, terminal output, badges |

All typefaces are available on Google Fonts / Bunny Fonts and are open-source friendly.

### Scale (base 16 px)

| Step | Size | Line height | Use |
|---|---|---|---|
| xs | 12 px | 1.5 | Captions, fine print |
| sm | 14 px | 1.5 | Secondary labels |
| base | 16 px | 1.6 | Body copy |
| lg | 18 px | 1.5 | Lead paragraphs |
| xl | 24 px | 1.3 | H3 |
| 2xl | 32 px | 1.2 | H2 |
| 3xl | 48 px | 1.1 | H1 |
| display | 64 px | 1.0 | Hero headlines |

---

## Tone & voice (brief)

- **Direct** — say what it does, not what it is.
- **Confident but not arrogant** — Ara is powerful; let the product speak.
- **Human** — write like a person, not a press release.

---

## Assets in this repository

```
branding/
  BRAND.md          ← this file
  logos/
    ara-logo-16.png
    ara-logo-32.png
    ara-logo-64.png
    ara-logo-256.png
    ara-logo-512.png  ← master
profile/
  logo.png          ← original source (512×512)
  hero.png          ← org profile hero banner
  README.md         ← GitHub org profile page
```

---

## Questions / updates

Open a PR targeting `main` in this repo. Tag a brand owner for review before merging color or logo changes.
