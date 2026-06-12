# scripts/

Utility scripts for the Ara org profile.

## validate_profile.py

Headless validator invoked by `.github/workflows/validate-profile.yml`.

**What it checks:**

- `profile/logo.png` — must be exactly 512×512 px and under 500 KB
- `profile/hero.png` — must be at least 1000 px wide, landscape aspect ratio, under 2 MB
- `profile/README.md` — must contain an `<h1>`, at least one link, and at least one image
- `CHANGELOG.md` — must exist and have at least one versioned entry (`## [vX.Y]`)
- All `<a href="...">` links in the README — probed with HTTP HEAD (GET fallback); failures are reported

**Outputs:**

- `validation-report.md` — uploaded as a workflow artifact
- GitHub issue filed under the `profile-validator` label (requires `GITHUB_TOKEN` with `issues: write`)
- Slack message via incoming webhook (requires `SLACK_WEBHOOK_URL` secret)

**Local usage:**

```bash
pip install pillow requests
python scripts/validate_profile.py
```
