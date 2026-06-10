# Ara Brand Assets

Documentation for canonical and derived brand assets in this repository.

## Canonical assets (`profile/`)

| File | Dimensions | Color mode | File size | Usage |
|------|-----------|------------|-----------|-------|
| `profile/hero.png` | 1280×768 | P (8-bit palette, pngquant) | 194 KB | GitHub org profile banner |
| `profile/hero.webp` | 1280×768 | RGB | 81 KB | Modern-browser hero (WebP fallback) |
| `profile/logo.png` | 512×512 | RGBA | 73 KB | Org logo / avatar source |
| `profile/logo.webp` | 512×512 | RGBA | 6 KB | Modern-browser logo (WebP fallback) |

## Derived assets (`assets/`)

| File | Dimensions | File size | Usage |
|------|-----------|-----------|-------|
| `assets/favicon.ico` | 16+32 multi | 2 KB | Browser tab icon (primary) |
| `assets/favicon-32x32.png` | 32×32 | 1 KB | Browser tab icon (PNG) |
| `assets/favicon-16x16.png` | 16×16 | 1 KB | Browser tab icon (small) |
| `assets/logo-200x200.png` | 200×200 | 18 KB | Social avatar / profile photo |

## Platform rendering notes

- **GitHub org profile banner** — GitHub displays `hero.png` at full width. Key content should stay within the central 960×480 safe zone to avoid cropping on smaller viewports.
- **GitHub org avatar** — GitHub crops `logo.png` to a circle at 460×460 px; keep the primary subject within that radius.
- **OpenGraph / social share** — `hero.png` at 1280×768 works as an OG image with slight letterboxing (ideal spec is 1200×630).
- **Twitter/X large card** — minimum 300×157; `hero.png` exceeds this and works as `summary_large_image`.
- **Social avatar** — `logo-200x200.png` is displayed at 48–200 px, usually cropped to circle.

## Export settings

- **Color space:** sRGB
- **hero.png:** lossy pngquant quantization, quality 70–90, compress_level 9; converted from 24-bit RGB → 8-bit palette. Saves ~66% vs the original 24-bit PNG.
- **logo.png:** lossless PNG re-encoded at compress_level 9; EXIF (336 bytes) and Adobe XMP (1631 bytes) stripped.
- **hero.webp / logo.webp:** lossy WebP, quality 80, method 6; generated from clean (EXIF-stripped) source.
- **EXIF policy:** all EXIF metadata stripped at export; no design-tool IDs or creator names are embedded.

## Recommended HTML favicon snippet

```html
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
```

## Updating assets

1. Export from your design tool at native resolution.
2. Strip EXIF before committing — run `python3 scripts/strip_exif.py <file>` or use the Pillow round-trip in the bg-agent recipe.
3. Regenerate derived assets by re-running the Pillow script in `scripts/` (to be added).
4. For hero.png, run `pngquant --quality=70-90 --speed 1 --force --output hero.png hero.png` after EXIF strip.
5. Generate WebP variants alongside every PNG update.

## Asset status

| File | Status | Notes |
|------|--------|-------|
| `profile/hero.png` | ✓ Optimized | EXIF stripped, pngquant compressed; was 574 KB → now 194 KB |
| `profile/logo.png` | ✓ Optimized | EXIF + Adobe XMP stripped; was 94 KB → now 73 KB |
| `profile/hero.webp` | ✓ New | WebP variant for modern browsers |
| `profile/logo.webp` | ✓ New | WebP variant for modern browsers |
| `assets/favicon.*` | ✓ New | Derived from logo.png |
| `assets/logo-200x200.png` | ✓ New | Social avatar derived from logo.png |
