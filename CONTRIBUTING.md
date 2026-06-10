# Contributing

This repository holds the GitHub organisation profile for [Ara](https://ara.so).

## Structure

- `profile/README.md` — the rendered org profile page on GitHub
- `profile/hero.png` — hero banner image
- `profile/logo.png` — logo displayed in the profile

## Making changes

1. Edit `profile/README.md` for copy or layout changes.
2. Replace `profile/hero.png` or `profile/logo.png` with optimised images (PNG, ≤ 600 KB each recommended).
3. Open a pull request. CI will lint Markdown and verify all required assets are present.

## CI checks

The `Profile CI` workflow runs on every push and pull request:

- **Markdown lint** — `markdownlint-cli` with the rules in `.markdownlintrc`
- **Asset validation** — `scripts/validate-profile.js` confirms `hero.png` and `logo.png` exist

## Image optimisation tips

Use `pngquant` or `optipng` to reduce PNG size before committing:

```bash
pngquant --force --quality=65-80 profile/hero.png -o profile/hero.png
optipng -o5 profile/logo.png
```
