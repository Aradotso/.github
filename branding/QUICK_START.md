# Ara brand quick start

Use this guide when creating Ara public profile pages, website sections, app surfaces, launch assets, and social previews. It is based on the assets in this repository and the public `ara.so` design tokens available at the time this guide was written.

## Logo variants

Use `profile/logo.png` for the default Ara mark. It is a square 512 × 512 PNG and should be used anywhere the mark needs to stand alone.

Use `profile/hero.png` for wide brand moments. It is a 1280 × 768 image and works best as a GitHub organization profile hero, open graph preview, landing page masthead, press kit preview, or deck cover.

Use `profile/logo.png` at 120 px wide for the GitHub profile README and similar centered profile treatments. Keep the mark visually quiet and pair it with a text link to `https://www.ara.so` rather than adding extra taglines.

Use `profile/logo.png` for app icons, dock-style icons, favicons, avatars, and small square social icons. Export down from the 512 px source and keep the full square canvas; do not crop into the mark.

Use `profile/hero.png` for social cards only when the destination supports wide imagery. For small circular avatars, use `profile/logo.png` instead.

## Primary color palette

The brand is intentionally neutral and system-native. Prefer semantic tokens over hard-coded color names so light and dark surfaces can switch cleanly.

`--ara-bg`: `#f7f7f7`, RGB `247 247 247`. Default app and website background.

`--ara-bg-elevated`: `#ffffff`, RGB `255 255 255`. Raised cards, panels, popovers, and profile surfaces.

`--color-bg-alt`: `#f5f5f5`, RGB `245 245 245`. Alternate section background when a page needs subtle separation.

`--ara-text`: `#111111`, RGB `17 17 17`. Primary text and high-emphasis foreground.

`--color-text`: `#1c1917`, RGB `28 25 23`. Stone-toned text token inherited from the website theme.

`--ara-text-body`: `rgba(17, 17, 17, .7)`. Long-form body copy and supporting descriptions.

`--color-text-secondary`: `#78716c`, RGB `120 113 108`. Secondary labels, metadata, and muted navigation items.

`--color-text-tertiary`: `#a8a29e`, RGB `168 162 158`. Tertiary text, placeholders, and low-emphasis helper copy.

`--ara-border`: `#e7e5e4`, RGB `231 229 228`. Dividers, card strokes, and hairline borders.

`--ara-cta-bg`: `#111111`, RGB `17 17 17`. Primary call-to-action background on light surfaces.

`--ara-cta-text`: `#ffffff`, RGB `255 255 255`. Primary call-to-action text on `--ara-cta-bg`.

For dark mode, use `--ara-bg: #141414`, RGB `20 20 20`; `--ara-bg-elevated: #1f1e1d`, RGB `31 30 29`; `--ara-border: #2f2d2b`, RGB `47 45 43`; `--ara-text: #ffffff`, RGB `255 255 255`; and keep muted text as white alpha values from the site tokens.

## Typography scale

Use the site token family for product, website, and profile copy: `--font-sans: system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif`. Use the same stack for mono/code until a dedicated mono token is introduced: `--font-mono: system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif`.

Use `--text-xs: .75rem` with `--text-xs--line-height: calc(1 / .75)` for captions, badges, timestamps, and compact metadata.

Use `--text-sm: .875rem` with `--text-sm--line-height: calc(1.25 / .875)` for labels, helper text, compact buttons, and navigation.

Use `--text-base: 1rem` with `--text-base--line-height: 1.5` for normal UI copy and short paragraphs.

Use `--text-lg: 1.125rem` with `--text-lg--line-height: calc(1.75 / 1.125)` for emphasized body copy and lead text.

Use `--text-xl: 1.25rem` with `--text-xl--line-height: calc(1.75 / 1.25)` for card titles and section eyebrow pairings.

Use `--text-2xl: 1.5rem` with `--text-2xl--line-height: calc(2 / 1.5)` for modal titles, feature headings, and compact page titles.

Use `--text-3xl: 1.875rem` with `--text-3xl--line-height: 1.2` for section headings.

Use `--text-4xl: 2.25rem` with `--text-4xl--line-height: calc(2.5 / 2.25)` for marketing page headings on small screens.

Use `--text-5xl: 3rem`, `--text-6xl: 3.75rem`, `--text-8xl: 6rem`, or `--text-9xl: 8rem` with line-height `1` for large brand moments and hero headlines.

Use `--font-weight-normal: 400` for most copy, `--font-weight-medium: 500` for UI emphasis, `--font-weight-semibold: 600` for compact headings, and `--font-weight-extrabold: 800` only for rare campaign-style impact.

Use `--tracking-tight: -.025em` for large headings, `--tracking-normal: 0em` for body copy, and `--tracking-wide: .025em` for small uppercase captions.

## Spacing and grid rules

Base spacing comes from `--spacing: .25rem`, so use 4 px increments for padding, gap, margin, and layout offsets.

Use 4 px, 8 px, 12 px, and 16 px for dense UI spacing. Use 24 px and 32 px for card padding, section rhythm, and profile README image spacing. Use 80 px vertical padding for full-width website sections when mirroring `ara.so`.

Use container tokens for readable widths: `--container-sm: 24rem`, `--container-md: 28rem`, `--container-lg: 32rem`, `--container-xl: 36rem`, `--container-2xl: 42rem`, `--container-3xl: 48rem`, `--container-4xl: 56rem`, and `--container-5xl: 64rem`.

Keep profile and README content centered. Use the logo at 120 px wide in simple profile contexts and allow the hero image to span the available README width.

For website layouts, use responsive grids with 16 px mobile gutters, 24 px tablet gutters, and 32 px desktop gutters. Prefer 12-column desktop grids for marketing pages and 4-column or single-column grids for app/editor surfaces.

Use radius tokens from the site scale: `--radius-sm: .25rem`, `--radius-md: .375rem`, `--radius-lg: .5rem`, `--radius-xl: .75rem`, `--radius-2xl: 1rem`, and `--radius-3xl: 1.5rem`. Marketing sections can use 24 px rounding; UI controls should stay closer to 4–12 px.

## Dos and don'ts

Do use the existing PNG assets before introducing new exported marks.

Do keep the mark on quiet white, off-white, or dark neutral surfaces.

Do preserve the square logo canvas and the wide hero aspect ratio.

Do use token names in code and design handoff notes so future palette changes are centralized.

Do use system fonts to match the current product and website feel.

Do keep brand layouts minimal, spacious, and low-chroma.

Don't recolor, stretch, crop, rotate, outline, shadow, or add effects to the logo.

Don't place the logo on busy photography, gradients, or low-contrast surfaces.

Don't mix in unrelated accent colors unless they are part of a product state such as success, warning, error, or third-party brand integration.

Don't replace the system font stack with a decorative brand font without updating the shared tokens first.

Don't use the wide hero image where a square avatar or small app icon is required.

Don't create new spacing values when a 4 px token increment works.

## Shared design links

Public website reference: https://www.ara.so

Shared Figma file: none found in this repository. Add the canonical link here when it is published.

Storybook: none found in this repository. Add the canonical link here when it is available.
