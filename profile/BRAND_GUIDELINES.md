# Ara Brand Guidelines

This document captures Ara's visual and verbal identity for contributors, contractors, and anyone producing materials that represent the Ara brand.

---

## Color Palette

Ara's palette is warm stone — grounded, quiet, and fast. There is no vivid brand color; the hierarchy comes from contrast and weight.

**Light mode**

| Role | Token | Hex |
|---|---|---|
| Page background | `--color-bg` | `#fafaf9` |
| Alt / sidebar background | `--color-bg-alt` | `#edeceb` |
| Surface (cards, panels) | `--color-surface` | `#ffffff` |
| Default border | `--color-border` | `#e7e5e4` |
| Hover border | `--color-border-hover` | `#d6d3d1` |
| Primary text | `--color-text` | `#1c1917` |
| Secondary text | `--color-text-secondary` | `#78716c` |
| Subtle / tertiary text | `--color-text-subtle` | `#a8a29e` |
| Primary accent (interactive) | `--color-accent` | `#1c1917` |
| Accent hover | `--color-accent-hover` | `#57534e` |
| Success | `--color-success` | `#16a34a` |
| Error | `--color-error` | `#FF3535` |
| Warning | `--color-warning` | `#f59e0b` |

**Dark mode** — backgrounds invert to `#111110`–`#1f1e1d`, primary text becomes `#f5f5f4`. All stone tones; nothing electric.

Use these tokens (or their direct hex equivalents) in any frontend work, pitch decks, or marketing assets. Do not introduce new brand colors without a design review.

---

## Typography

Three font families cover all use cases.

**Inter** — primary sans-serif. Used for all body copy, labels, navigation, and UI text. Load weights 400–700. Variable font preferred where available.

**Instrument Serif** — display accent. Used for hero headlines, editorial moments, and anywhere the product needs warmth or personality. Regular and Italic only.

**JetBrains Mono** — monospace. Used for code samples, terminal output, inline code, and any technical string the user needs to read precisely. Weights 400–500.

CSS variables: `--font-sans`, `--font-serif`, `--font-mono`. Always reference these variables in frontend code rather than hard-coding the family names so the design system remains swappable.

---

## Logo Usage

The Ara logo lives in `profile/logo.png`. The hero banner lives in `profile/hero.png`.

**Sizing** — the minimum clear display size for the logo is 32 × 32 px. The canonical profile display size is 120 px wide (as used in the GitHub org README). Never scale below 24 px.

**Clear space** — maintain at least half the logo's width as clear space on all sides. Do not place other elements inside that margin.

**Do not** — stretch, rotate, recolor, add drop shadows, place on a busy background, or modify the logo file. If you need a variant (e.g., white version for dark backgrounds), request it from the design team rather than editing the asset yourself.

**File formats** — use the PNG for web and documents. Ask for an SVG or high-resolution export when producing print, video, or large-format work.

---

## Tone of Voice

Ara speaks concisely and acts. The voice is direct, confident, and technical without being cold. A few rules:

- **Short sentences win.** If a sentence can be cut in half, cut it.
- **Action over description.** Say what Ara does, not what it is. "Ara runs the build and pushes the branch" beats "Ara is an intelligent agent that can automate build and branch operations."
- **No filler.** Cut "just", "simply", "very", "really", "basically", and throat-clearing phrases like "In order to…"
- **Second person, present tense.** Write for what the user is doing right now.
- **Confident but not boastful.** State capabilities plainly; let them speak for themselves.
- **Technical specificity is a feature.** Prefer exact names (`git push`, `pnpm dev`) over vague gestures ("run the command").

This tone applies to UI copy, documentation, commit messages, PR descriptions, error messages, and any communication that goes out under the Ara brand.

---

## Imagery Style

Ara visuals are minimal, warm, and purposeful. No decorative clutter.

**Photography / illustrations** — neutral or warm-toned, not cold or blue. Clean backgrounds. Subject matter tends toward workspaces, tools, and interfaces rather than abstract shapes or stock "team" photos.

**UI screenshots** — always captured at 2× (Retina) resolution. Use the light-mode palette unless specifically showing dark mode. Crop tightly to the relevant area; do not show an entire browser chrome unless the browser chrome is the point.

**Motion / video** — transitions are quick and functional (200–300 ms). No gratuitous animations. Easing is ease-out or ease-in-out; never linear or bounce.

**Iconography** — line icons, consistent stroke weight (1.5–2 px at 24 px baseline). Do not mix filled and outline styles in the same UI context.

---

## Contributing

If you are producing new assets or copy for Ara, start here. When in doubt, default to restraint: less color, fewer words, tighter layout. Open a discussion or ping the design team before introducing anything that deviates materially from this guide.

See [CONTRIBUTING.md](./CONTRIBUTING.md) for code and workflow conventions.
