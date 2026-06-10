# Ara Brand Assets

This directory holds derived and supplementary brand assets generated from the canonical sources in `profile/`.

## Canonical Assets (`profile/`)

### hero.png
- Dimensions: 1280 × 768 px
- Color mode: RGB (no alpha)
- File size: ~567 KB (EXIF stripped)
- Format: PNG, sRGB color space
- Usage: GitHub org profile banner, website hero images, press kit
- Recommended display width: 1280 px max; scales down to 640 px on mobile
- Export settings: PNG-24, no alpha, sRGB, 72 dpi, no EXIF metadata

### logo.png
- Dimensions: 512 × 512 px
- Color mode: RGBA (transparent background)
- File size: ~75 KB (EXIF stripped)
- Format: PNG, gamma-corrected (γ = 1/2.2), 96 dpi
- Usage: GitHub org avatar, app icon source, dark/light backgrounds
- Recommended minimum display size: 24 × 24 px
- Export settings: PNG-32, RGBA, sRGB, 96 dpi, no EXIF metadata

## Derived Assets (`assets/`)

| File | Dimensions | Format | Usage |
|------|-----------|--------|-------|
| `favicon.ico` | 16×16, 32×32 (multi-size) | ICO | Browser favicon, `<link rel="icon">` |
| `favicon-32x32.png` | 32 × 32 px | PNG (RGBA) | Modern browser favicon, Twitter/X card |
| `favicon-16x16.png` | 16 × 16 px | PNG (RGBA) | Legacy browser tab favicon |
| `logo-200x200.png` | 200 × 200 px | PNG (RGBA) | Social profile avatar (LinkedIn, Twitter/X) |

All derived assets were generated from `profile/logo.png` using Lanczos resampling.

## Platform Rendering Notes

### GitHub Org Profile
- `hero.png` displays as a banner at the top of the org profile page. GitHub crops the center at smaller viewports; keep key content in the central 960 × 480 px safe zone.
- `logo.png` (512 × 512) exceeds GitHub's 460 × 460 org avatar cap — GitHub will downsample. The image is already square, so no cropping occurs.

### Web / Social Media
- OpenGraph images: use `hero.png` (1280 × 768) — matches the recommended 1200 × 630 OG spec closely; slight letterboxing may occur.
- Twitter/X card: `hero.png` covers the `summary_large_image` card format (min 300 × 157 px required; 1280 × 768 exceeds this).
- Social avatars: use `logo-200x200.png`; most platforms display at 48–200 px and crop to a circle.
- Favicons: reference `favicon.ico` as primary and `favicon-32x32.png` as PNG fallback in HTML `<head>`.

## Recommended `<head>` Snippet

```html
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
```

## Asset Status

The current `hero.png` and `logo.png` are considered final for the v1 brand. Refinement notes:

- `hero.png` is RGB only (no transparency). This is correct for banner/background use.
- `logo.png` has a transparent background — suitable for all placement contexts.
- EXIF metadata (including Canva doc ID, creator name, and internal Canva brand references) has been stripped from both files to avoid leaking internal tool metadata.
- Color profile: `logo.png` uses standard sRGB chromaticity; `hero.png` uses the sRGB IEC61966-2.1 color space. Both render consistently across browsers and OS color management.

## Updating Assets

1. Export source files from the original design tool (Figma, Canva, etc.) at the specified dimensions.
2. Strip EXIF metadata before committing: `exiftool -all= <file>` or re-export without metadata.
3. Regenerate derived assets from `logo.png` using the `scripts/generate-assets.py` script (if added).
4. Update this README if dimensions or formats change.
