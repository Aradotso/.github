#!/usr/bin/env python3
"""Validate the GitHub organization profile before publishing."""

from __future__ import annotations

import pathlib
import re
import struct
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROFILE = ROOT / "profile"
README = PROFILE / "README.md"
LOGO = PROFILE / "logo.png"
HERO = PROFILE / "hero.png"
REQUIRED_LINKS = (
    "https://www.ara.so",
)


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def png_dimensions(path: pathlib.Path) -> tuple[int, int]:
    if not path.exists():
        fail(f"missing image: {path.relative_to(ROOT)}")

    with path.open("rb") as handle:
        header = handle.read(24)

    if len(header) < 24 or not header.startswith(b"\x89PNG\r\n\x1a\n"):
        fail(f"{path.relative_to(ROOT)} must be a PNG")

    return struct.unpack(">II", header[16:24])


def validate_markdown(text: str) -> None:
    if not text.endswith("\n"):
        fail("profile/README.md must end with a newline")

    if re.search(r"[ \t]+\n", text):
        fail("profile/README.md must not contain trailing whitespace")

    if text.count("<h1") != 1:
        fail("profile/README.md must contain exactly one h1")

    if "<h1 align=\"center\">Ara</h1>" not in text:
        fail("profile/README.md must keep the centered Ara h1")

    for image in ("./hero.png", "./logo.png"):
        if image not in text:
            fail(f"profile/README.md must reference {image}")

    for link in REQUIRED_LINKS:
        if link not in text:
            fail(f"profile/README.md must include required social/link target: {link}")

    links = re.findall(r"href=\"([^\"]+)\"", text)
    insecure = [link for link in links if link.startswith("http://")]
    if insecure:
        fail(f"profile links must use https: {', '.join(insecure)}")

    unknown = [link for link in links if not link.startswith("https://")]
    if unknown:
        fail(f"profile links must be absolute https URLs: {', '.join(unknown)}")


def main() -> None:
    if not README.exists():
        fail("missing profile/README.md")

    text = README.read_text(encoding="utf-8")
    validate_markdown(text)

    logo_width, logo_height = png_dimensions(LOGO)
    if (logo_width, logo_height) != (512, 512):
        fail(f"profile/logo.png must be 512x512, got {logo_width}x{logo_height}")

    hero_width, hero_height = png_dimensions(HERO)
    if hero_width < 1200 or hero_height < 600:
        fail(f"profile/hero.png must be at least 1200x600, got {hero_width}x{hero_height}")

    print("Profile validation passed.")


if __name__ == "__main__":
    main()
