#!/usr/bin/env python3
import os
import re
import sys
from PIL import Image

def validate_profile(profile_dir="profile", readme_name="README.md"):
    readme_path = os.path.join(profile_dir, readme_name)
    if not os.path.exists(readme_path):
        print(f"FAIL: {readme_path} does not exist.")
        return False

    print(f"Validating {readme_path}...")
    errors = []
    warnings = []

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Spacing check (e.g., blank lines around fenced code blocks to prevent MD031)
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith("```"):
            # Check previous line if i > 0
            if i > 0 and lines[i - 1].strip() != "":
                warnings.append(f"Line {i+1}: Fenced code block starting with '```' should have a blank line before it to avoid MD031 markdown lint warning.")
            # Check next line if i < len(lines) - 1
            if i < len(lines) - 1 and lines[i + 1].strip() != "" and not lines[i + 1].strip().startswith("```"):
                pass # usually, we check ending fences too, but this is a good start

    # 2. Extract image links
    # Match markdown images: ![alt](path)
    md_images = re.findall(r'!\[(.*?)\]\((.*?)\)', content)
    # Match HTML images: <img ... src="path" ... alt="alt" ...>
    # To handle attributes in any order, let's find the entire <img ...> tag first
    html_img_tags = re.findall(r'<img\s+[^>]*src=["\'](.*?)["\'][^>]*>', content, re.IGNORECASE)

    # Let's verify all referenced images
    images_to_check = []
    
    for alt, src in md_images:
        images_to_check.append(("markdown", src.strip(), alt.strip()))

    for src in html_img_tags:
        # Try to find alt text inside the tag
        img_tag_match = re.search(rf'<img\s+[^>]*src=["\']{re.escape(src)}["\'][^>]*>', content, re.IGNORECASE)
        alt = ""
        if img_tag_match:
            tag_content = img_tag_match.group(0)
            alt_match = re.search(r'alt=["\'](.*?)["\']', tag_content, re.IGNORECASE)
            if alt_match:
                alt = alt_match.group(1).strip()
        images_to_check.append(("html", src.strip(), alt))

    if not images_to_check:
        warnings.append("No images found in profile/README.md.")

    for img_type, src, alt in images_to_check:
        print(f"Found image reference: src='{src}', alt='{alt}' ({img_type})")

        # Check for absolute paths or URLs (URLs are fine for external badges, but not local repo assets)
        if src.startswith("http://") or src.startswith("https://"):
            # It's an external URL. If it's supposed to be a profile asset, warn the user.
            if "github.com" in src and "profile" in src:
                warnings.append(f"Absolute URL used for profile asset: '{src}'. Consider using relative paths instead.")
            continue

        if src.startswith("/"):
            errors.append(f"Image path '{src}' is absolute relative to root. Use relative paths like './{src.lstrip('/')}' or '{src.lstrip('/')}'.")
            continue

        # Resolve relative path
        # Note: Paths inside profile/README.md are relative to the README's directory or repo root on GitHub.
        # Usually, they are relative to the directory they are in.
        target_path = os.path.normpath(os.path.join(profile_dir, src))

        # Check for case sensitivity issues by comparing actual directory listing
        target_dir = os.path.dirname(target_path)
        target_file = os.path.basename(target_path)

        if not os.path.exists(target_path):
            errors.append(f"Image '{src}' referenced in {readme_name} does not exist at '{target_path}'.")
            continue

        # Verify case-sensitivity match (vital for Linux-based GitHub runners/displays)
        if os.path.isdir(target_dir or '.'):
            actual_files = os.listdir(target_dir or '.')
            if target_file not in actual_files:
                # Find if there is a case-insensitive match
                ci_match = [f for f in actual_files if f.lower() == target_file.lower()]
                if ci_match:
                    errors.append(f"Case mismatch for image: referenced '{target_file}', actual file on disk is '{ci_match[0]}'. GitHub is case-sensitive!")
                else:
                    errors.append(f"Image file '{target_file}' not found in directory '{target_dir}'.")

        # Check Alt text
        if not alt:
            warnings.append(f"Image '{src}' is missing an alt description for accessibility.")

        # Check Image Properties via Pillow
        try:
            with Image.open(target_path) as img:
                w, h = img.size
                f_size = os.path.getsize(target_path)
                
                # Check for sRGB color space
                color_profile = img.info.get('icc_profile')
                # Check if it has sRGB or standard color spaces
                if img.mode not in ('RGB', 'RGBA'):
                    warnings.append(f"Image '{src}' uses non-standard color mode '{img.mode}'. Consider converting to RGB/RGBA.")
                
                # Check file size limits (Hero: 1MB, Logo: 200KB)
                if 'logo' in target_file.lower() and f_size > 200 * 1024:
                    warnings.append(f"Logo image '{src}' is quite large ({f_size/1024:.1f}KB). It should ideally be under 200KB.")
                elif 'hero' in target_file.lower() and f_size > 1024 * 1024:
                    warnings.append(f"Hero image '{src}' is very large ({f_size/1024/1024:.2f}MB). It should ideally be under 1MB.")
                
        except Exception as e:
            errors.append(f"Failed to open/parse image file '{target_path}': {e}")

    # Summary
    print("\n--- Validation Summary ---")
    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f" - {w}")
    else:
        print("No warnings.")

    if errors:
        print(f"FAILURES ({len(errors)}):")
        for e in errors:
            print(f" - {e}")
        return False
    else:
        print("SUCCESS: Profile verification passed successfully!")
        return True

if __name__ == "__main__":
    success = validate_profile()
    if not success:
        sys.exit(1)
