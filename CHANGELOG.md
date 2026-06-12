# Changelog

All notable changes to the Ara org profile are documented here.

## [Unreleased]

## [v0.2.0] - 2025-06-12

### Added
- GitHub Actions workflow (`validate-profile.yml`) that runs daily and on every
  profile change to automatically validate logo sizes, hero dimensions, social
  links, README markup, and CHANGELOG freshness.
- `scripts/validate_profile.py` — headless Python validator that checks all
  of the above and files a GitHub issue + posts a Slack notification when drift
  is detected.

## [v0.1.0] - 2025-06-02

### Added
- Initial org profile: `profile/README.md`, `profile/logo.png`, `profile/hero.png`.
- `ROADMAP.md` describing near-term priorities for the Ara platform.
