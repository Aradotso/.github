# Brand Asset Specifications

This document outlines the standard resolutions, color configurations, formats, and design settings for Ara branding and profile assets.

## Profile Hero Image

- File Path: profile/hero.png
- Dimensions: 1280 x 768 px
- Format: PNG
- Color Space: sRGB IEC61966-2.1 (8-bit per channel)
- Alpha Channel: No alpha (hasAlpha: no)
- Resolution/DPI: 72 DPI
- Usage: Main visual header banner at the top of the GitHub organization profile. Ensure visual elements are centered to prevent clipping on responsive grid sizes.

## Brand Logo

- File Path: profile/logo.png
- Dimensions: 512 x 512 px
- Format: PNG
- Color Space: sRGB IEC61966-2.1 (8-bit per channel)
- Alpha Channel: Yes (hasAlpha: yes)
- Resolution/DPI: 96 DPI
- Software Origin: Canva (Black and White Simple Modern Clean Creative Technology Logo template)
- Artist: Adi Singh
- Usage: Organization avatar, small-scale branding, and favicon-derived variants.

## Recommended Additional Brand Assets

To support web deployment, social shares, and application contexts, the following asset variants are recommended for future exports:

### Favicon Package
- favicon.ico: Multi-resolution (16x16, 32x32, 48x48 px) legacy format.
- icon.svg: Scalable vector format for modern browsers.
- apple-touch-icon.png: 180 x 180 px PNG with a solid background and padding, used for iOS home screens.

### Open Graph / Social Media Preview (og:image)
- Dimensions: 1200 x 630 px PNG
- Aspect Ratio: 1.91:1
- Safe Zone: Keep critical text and logo marks within a central 640 x 360 px area to avoid truncation on modern link previews (Slack, X, LinkedIn, iMessage).
- Color Space: sRGB IEC61966-2.1 (required for correct color rendering across diverse mobile and desktop display systems).
