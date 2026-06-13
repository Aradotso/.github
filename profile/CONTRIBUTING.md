# Contributing to the Ara GitHub profile

This repository powers the public GitHub organization profile shown from `profile/README.md`. Treat it as a small public publishing surface: keep it aligned with canonical Ara messaging, validate every visual/link change, and avoid turning it into a general product documentation repo.

## Canonical source sync

Profile updates should start from approved public or internal canonical sources, then be rewritten for a public GitHub audience.

- Public source of truth: use the current public website at [ara.so](https://www.ara.so) for company name, tagline, product positioning, and primary call-to-action links.
- Internal source of truth: use approved internal docs only for messaging that is already cleared for public release. Do not copy private roadmap, customer, hiring, investor, security, or operations details into the profile.
- Asset source of truth: sync logos, hero art, and brand imagery from the approved brand source, then commit optimized files under `profile/` with local relative references such as `./logo.png`.
- Copy sync rule: when ara.so and an internal draft disagree, keep the public website wording unless a maintainer explicitly approves a messaging refresh.
- Review rule: any change that introduces new product claims, customer claims, screenshots, or team information needs maintainer review before merge.

Useful Ara workflow patterns for this repository are the `ara-bg-agent-write-repo-docs`, `ara-bg-agent-profile-health-checks`, `ara-bg-agent-profile-sync`, and `background-coding-workflows` skills. Load those skills before changing automation or profile-maintenance documentation so future updates follow the same conventions.

## Profile health checks

A profile update is healthy when it renders cleanly on GitHub, keeps the public brand consistent, and avoids broken links. Validate these rules before opening or merging a PR.

### Logo and image rules

- `profile/logo.png` should remain a square transparent PNG, currently `512x512`, and be rendered from Markdown/HTML at a small display width such as `120`.
- Keep `profile/logo.png` below `1 MB`; target substantially smaller when compression does not damage the mark.
- `profile/hero.png` should remain landscape artwork, currently `1280x768`, and should stay below `1 MB` unless a maintainer approves a higher-quality replacement.
- All README image references should be local relative paths under `profile/` so the GitHub profile renders without external image hosts.
- Every image needs descriptive alt text; avoid generic labels like `image` or `banner`.

### Link and social rules

- Public links must use `https://` URLs.
- Prefer canonical Ara domains, especially [https://www.ara.so](https://www.ara.so), unless the profile intentionally links to a verified social or product surface.
- Social links must point to official Ara-owned accounts. Do not add personal accounts as company social links.
- New links should be checked for successful responses and should not redirect through tracking shorteners.
- Keep link text human-readable, for example `ara.so` instead of a raw long URL.

### Markdown and rendering rules

- Run Markdown linting for all files under `profile/`.
- Inline HTML is allowed in `profile/README.md` when needed for GitHub profile centering or image sizing.
- Do not weaken Markdown linting for new prose. If a lint exception is needed, document it in `.markdownlint-cli2.jsonc` and keep the exception scoped to profile rendering needs.
- Keep the README concise enough to render well in GitHub's organization profile card.
- Run whitespace checks before commit so trailing spaces and conflict markers do not ship.

## Run validation locally

From the repository root, run the same lightweight checks expected in CI:

```sh
npx --yes markdownlint-cli2 "profile/**/*.md"
git diff --check
python3 - <<'PY'
from pathlib import Path
from PIL import Image

checks = {
    "profile/logo.png": {"max_bytes": 1_000_000, "square": True},
    "profile/hero.png": {"max_bytes": 1_000_000, "landscape": True},
}

for name, rules in checks.items():
    path = Path(name)
    if not path.exists():
        raise SystemExit(f"missing {name}")
    with Image.open(path) as image:
        width, height = image.size
    if rules.get("square") and width != height:
        raise SystemExit(f"{name} must be square, got {width}x{height}")
    if rules.get("landscape") and width <= height:
        raise SystemExit(f"{name} must be landscape, got {width}x{height}")
    if path.stat().st_size > rules["max_bytes"]:
        raise SystemExit(f"{name} is too large: {path.stat().st_size} bytes")
    print(f"{name}: {width}x{height}, {path.stat().st_size} bytes")
PY
```

If Pillow is not installed locally, install it in a temporary virtual environment or use an equivalent image-inspection command. Do not commit local virtual environment files.

## CI/CD and approvals

The profile has a simple publishing flow:

- Background agents or contributors open a branch and PR for profile changes.
- CI should run Markdown linting, profile asset validation, social/link validation, and whitespace checks.
- A maintainer reviews the PR for public messaging, brand safety, and source-of-truth alignment.
- After approval, the PR merges to `main`.
- GitHub renders `profile/README.md` on the organization profile automatically after the merge; there is no separate production deploy for this repository.

Approval expectations:

- Routine typo, formatting, or link maintenance can be approved by one maintainer.
- New team-member mentions, new logos, or messaging refreshes need brand/source-of-truth review.
- Changes based on internal docs must say which approved source was used in the PR description without pasting private content.
- Automation changes should reference the Ara skill pattern that guided the update, such as `ara-bg-agent-profile-health-checks` or `ara-bg-agent-write-repo-docs`.

## Common profile updates

### Add a new team member mention

1. Confirm the person should be public on GitHub and that their name/title matches the approved public source.
2. Add the shortest useful mention to `profile/README.md`; avoid bios, private team structure, or internal responsibilities.
3. If linking a profile, use an official public profile that the person has approved.
4. Run Markdown linting and link validation before PR.
5. Note the approved source in the PR body.

### Replace the logo

1. Export the approved logo from the brand source as a transparent square PNG.
2. Optimize it and replace `profile/logo.png` without changing the filename unless required.
3. Keep the rendered width in `profile/README.md` small enough for the GitHub profile card.
4. Confirm the file is square, below the size budget, and has descriptive alt text.
5. Include a before/after screenshot or asset note in the PR when available.

### Refresh messaging

1. Start from the current website copy at [ara.so](https://www.ara.so) or an approved internal messaging doc.
2. Rewrite for GitHub: short, public, and durable.
3. Remove claims that depend on private customer, roadmap, or fundraising context.
4. Update links only when the canonical destination changed.
5. Request maintainer review for source alignment before merge.

### Add or update a social link

1. Verify the account is official and active.
2. Use the canonical `https://` profile URL without tracking parameters.
3. Use clear link text such as `X`, `LinkedIn`, or `YouTube` only when the destination is official.
4. Check the link locally and in the PR preview.
5. Remove stale social links instead of leaving dead destinations in the public profile.
