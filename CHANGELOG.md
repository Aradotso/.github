# Changelog

All notable changes to the Ara org profile are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [1.1.0] – 2026-06-11

### Added
- Automated profile health-check workflow (`.github/workflows/profile-health-check.yml`)
  that runs every Monday at 09:00 UTC (and on relevant `main` pushes).
- `scripts/profile_health_check.py` — validates logo dimensions (512 × 512 RGBA),
  hero image minimum size (1280 × 640), README social links (HTTP reachability),
  README HTML tag balance, and CHANGELOG freshness.
- This `CHANGELOG.md` to track profile evolution.
- Workflow files GitHub issues and/or posts to Slack when drift is detected.

## [1.0.0] – 2025-03-01

### Added
- Initial org profile with `hero.png`, `logo.png`, and `README.md`.
