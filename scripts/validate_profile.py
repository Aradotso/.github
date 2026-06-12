#!/usr/bin/env python3
"""
Org profile validator for Aradotso/.github
Checks:
  1. Logo dimensions (expect 512×512)
  2. Hero dimensions (expect 1280×640 or wider landscape)
  3. Social / homepage links resolve with 2xx
  4. README.md markup (required tags, non-empty)
  5. CHANGELOG.md exists and has at least one versioned entry
  6. Image file sizes are within reasonable bounds

On failure: files a GitHub issue and/or posts a Slack notification.
"""

import json
import os
import re
import sys
from pathlib import Path

import requests
from PIL import Image

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

PROFILE_DIR = Path(__file__).parent.parent / "profile"
README_PATH = PROFILE_DIR / "README.md"
CHANGELOG_PATH = Path(__file__).parent.parent / "CHANGELOG.md"
LOGO_PATH = PROFILE_DIR / "logo.png"
HERO_PATH = PROFILE_DIR / "hero.png"

LOGO_EXPECTED_SIZE = (512, 512)
LOGO_MAX_BYTES = 500_000      # 500 KB
HERO_MIN_WIDTH = 1000         # px
HERO_ASPECT_RATIO_FLOOR = 1.3 # width/height >= 1.3 (landscape)
HERO_MAX_BYTES = 2_000_000    # 2 MB

REQUIRED_README_ELEMENTS = [
    r'<h1[^>]*>',        # heading
    r'<a\s+href=',       # at least one link
    r'<img\s+src=',      # at least one image
]

SOCIAL_LINKS_IN_README = True   # extract and probe all <a href="..."> in README

VERSION_RE = re.compile(r'^##\s+\[?v?\d+\.\d+', re.MULTILINE)

GITHUB_API = "https://api.github.com"
GITHUB_REPO = os.environ.get("GITHUB_REPOSITORY", "Aradotso/.github")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL", "")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

failures: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    print(f"  FAIL  {msg}")
    failures.append(msg)


def warn(msg: str) -> None:
    print(f"  WARN  {msg}")
    warnings.append(msg)


def ok(msg: str) -> None:
    print(f"  OK    {msg}")


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_image(path: Path, expected_size: tuple[int, int] | None,
                min_width: int | None, aspect_floor: float | None,
                max_bytes: int, label: str) -> None:
    if not path.exists():
        fail(f"{label}: file not found at {path}")
        return

    size = path.stat().st_size
    if size > max_bytes:
        fail(f"{label}: file size {size:,} bytes exceeds limit {max_bytes:,} bytes")
    else:
        ok(f"{label}: size {size:,} bytes")

    try:
        img = Image.open(path)
        w, h = img.size
    except Exception as exc:
        fail(f"{label}: cannot open image — {exc}")
        return

    if expected_size:
        if (w, h) != expected_size:
            fail(f"{label}: dimensions {w}×{h} (expected {expected_size[0]}×{expected_size[1]})")
        else:
            ok(f"{label}: dimensions {w}×{h} ✓")

    if min_width and w < min_width:
        fail(f"{label}: width {w}px is below minimum {min_width}px")

    if aspect_floor and h > 0:
        ratio = w / h
        if ratio < aspect_floor:
            fail(f"{label}: aspect ratio {ratio:.2f} is below landscape floor {aspect_floor}")
        else:
            ok(f"{label}: aspect ratio {ratio:.2f} ✓")


def check_readme() -> list[str]:
    if not README_PATH.exists():
        fail("README.md: file not found")
        return []

    content = README_PATH.read_text(encoding="utf-8")
    if len(content.strip()) < 20:
        fail("README.md: appears to be empty or nearly empty")
        return []
    else:
        ok(f"README.md: {len(content)} bytes")

    for pattern in REQUIRED_README_ELEMENTS:
        if not re.search(pattern, content, re.IGNORECASE):
            fail(f"README.md: missing required element matching /{pattern}/")
        else:
            ok(f"README.md: found /{pattern}/")

    # Extract all href values for link probing
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    return hrefs


def check_changelog() -> None:
    if not CHANGELOG_PATH.exists():
        warn("CHANGELOG.md: file not found (consider adding one)")
        return

    content = CHANGELOG_PATH.read_text(encoding="utf-8")
    matches = VERSION_RE.findall(content)
    if not matches:
        fail("CHANGELOG.md: no versioned entries found (expected '## [vX.Y]' or '## vX.Y')")
    else:
        ok(f"CHANGELOG.md: {len(matches)} versioned entries found")


def check_links(hrefs: list[str]) -> None:
    if not hrefs:
        warn("No links found in README to probe")
        return

    session = requests.Session()
    session.headers["User-Agent"] = "Ara-Profile-Validator/1.0"

    for url in hrefs:
        if not url.startswith("http"):
            continue
        try:
            resp = session.head(url, timeout=10, allow_redirects=True)
            if resp.status_code < 400:
                ok(f"Link {url} → {resp.status_code}")
            else:
                # Some servers reject HEAD — try GET
                resp2 = session.get(url, timeout=10, allow_redirects=True, stream=True)
                if resp2.status_code < 400:
                    ok(f"Link {url} → {resp2.status_code} (GET fallback)")
                else:
                    fail(f"Link {url} → HTTP {resp2.status_code}")
        except requests.RequestException as exc:
            fail(f"Link {url} unreachable — {exc}")


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def write_report() -> None:
    lines = ["# Org Profile Validation Report\n"]
    if failures:
        lines.append(f"**{len(failures)} failure(s) detected**\n")
        for f in failures:
            lines.append(f"- ❌ {f}")
    else:
        lines.append("✅ All checks passed\n")
    if warnings:
        lines.append(f"\n**{len(warnings)} warning(s)**\n")
        for w in warnings:
            lines.append(f"- ⚠️ {w}")
    Path("validation-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def file_github_issue() -> None:
    if not GITHUB_TOKEN:
        print("GITHUB_TOKEN not set — skipping issue creation")
        return

    title = f"[profile-validator] {len(failures)} validation failure(s) detected"
    body_lines = ["Automated profile validation found the following failures:\n"]
    for f in failures:
        body_lines.append(f"- {f}")
    body_lines += [
        "",
        "_This issue was filed automatically by the [Validate Org Profile]"
        "(.github/workflows/validate-profile.yml) workflow._",
    ]

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    # Check for existing open issue with same title to avoid duplicates
    search_url = f"{GITHUB_API}/repos/{GITHUB_REPO}/issues"
    existing = requests.get(search_url, headers=headers,
                            params={"state": "open", "labels": "profile-validator"},
                            timeout=15)
    for issue in existing.json() if existing.ok else []:
        if isinstance(issue, dict) and issue.get("title", "").startswith("[profile-validator]"):
            print(f"Existing open issue #{issue['number']} found — skipping duplicate")
            return

    resp = requests.post(
        f"{GITHUB_API}/repos/{GITHUB_REPO}/issues",
        headers=headers,
        json={
            "title": title,
            "body": "\n".join(body_lines),
            "labels": ["profile-validator"],
        },
        timeout=15,
    )
    if resp.ok:
        print(f"Filed issue #{resp.json().get('number')}: {title}")
    else:
        print(f"Failed to file issue: {resp.status_code} {resp.text[:200]}")


def post_slack(message: str) -> None:
    if not SLACK_WEBHOOK_URL:
        return
    try:
        resp = requests.post(
            SLACK_WEBHOOK_URL,
            json={"text": message},
            timeout=10,
        )
        if resp.ok:
            print("Slack notification sent")
        else:
            print(f"Slack notification failed: {resp.status_code}")
    except requests.RequestException as exc:
        print(f"Slack notification error: {exc}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("=== Ara Org Profile Validator ===\n")

    print("-- Logo --")
    check_image(
        LOGO_PATH,
        expected_size=LOGO_EXPECTED_SIZE,
        min_width=None,
        aspect_floor=None,
        max_bytes=LOGO_MAX_BYTES,
        label="logo.png",
    )

    print("\n-- Hero --")
    check_image(
        HERO_PATH,
        expected_size=None,
        min_width=HERO_MIN_WIDTH,
        aspect_floor=HERO_ASPECT_RATIO_FLOOR,
        max_bytes=HERO_MAX_BYTES,
        label="hero.png",
    )

    print("\n-- README --")
    hrefs = check_readme()

    print("\n-- CHANGELOG --")
    check_changelog()

    print("\n-- Social/Homepage Links --")
    check_links(hrefs)

    print("\n=================================")
    print(f"Result: {len(failures)} failure(s), {len(warnings)} warning(s)")

    write_report()

    if failures:
        file_github_issue()
        slack_msg = (
            f":warning: *Ara org profile validation failed* "
            f"({len(failures)} issue(s) in `{GITHUB_REPO}`):\n"
            + "\n".join(f"• {f}" for f in failures)
        )
        post_slack(slack_msg)
        return 1

    if warnings:
        post_slack(
            f":information_source: Org profile OK with {len(warnings)} warning(s) "
            f"in `{GITHUB_REPO}`."
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
