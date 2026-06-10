# Contributing to Ara

Thanks for your interest in contributing. This repo hosts the GitHub org profile for [Ara](https://ara.so) and shared project tooling.

## What lives here

- `profile/` — GitHub org profile files displayed on the Ara org page
- `scripts/` — helper scripts for validation
- `.github/workflows/` — CI configuration

## Making changes

1. Fork the repo and create a branch from `main`.
2. Make your changes.
3. Run `make lint` to check Markdown formatting and `make validate` to verify profile assets.
4. Commit with a clear message describing what changed and why.
5. Open a pull request targeting `main`.

## Commit style

Use a short imperative subject line (max 72 chars). Add a blank line then a body if extra context is needed.

Examples:

- `profile: update hero image`
- `ci: add Node 20 to test matrix`
- `docs: fix typo in CONTRIBUTING`

## Profile assets

The `profile/` directory contains:

- `README.md` — the org profile displayed on github.com/Aradotso
- `hero.png` — banner image shown at the top of the profile
- `logo.png` — square logo used in the profile body

All three are required. The CI `validate` job will fail if any are missing.

## Running locally

```sh
npm install       # install dev dependencies
make lint         # lint Markdown
make validate     # check required assets exist
```

## Questions

Open an issue or reach out at [sven@ara.so](mailto:sven@ara.so).
