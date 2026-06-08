#!/usr/bin/env python3
import os
import sys
import argparse
import shutil
import urllib.request
import re
from urllib.parse import urljoin, urlparse

# Import validation and optimization logic to invoke them programmatically
from validate_profile import validate_profile
from optimize_images import optimize_image

def download_file(url, dest_path):
    print(f"Downloading {url} to {dest_path}...")
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
        )
        with urllib.request.urlopen(req, timeout=15) as response, open(dest_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def sync_from_local(source_dir, profile_dir="profile"):
    print(f"Syncing locally from {source_dir}...")
    readme_src = os.path.join(source_dir, "README.md")
    if not os.path.exists(readme_src):
        # Look for index.html or other documentation if README not found
        readme_src = os.path.join(source_dir, "index.html")
        if not os.path.exists(readme_src):
            print(f"Error: No README.md or index.html found in source directory {source_dir}.")
            return False

    readme_dest = os.path.join(profile_dir, "README.md")
    shutil.copy2(readme_src, readme_dest)
    print(f"Copied {readme_src} to {readme_dest}")

    # Copy common branding assets if they exist in source
    for asset in ["logo.png", "hero.png", "logo.jpg", "hero.jpg", "logo.svg"]:
        asset_src = os.path.join(source_dir, asset)
        if os.path.exists(asset_src):
            asset_dest = os.path.join(profile_dir, asset)
            shutil.copy2(asset_src, asset_dest)
            print(f"Copied asset: {asset_src} to {asset_dest}")
            
    return True

def sync_from_url(url, profile_dir="profile"):
    print(f"Syncing remotely from URL {url}...")
    readme_dest = os.path.join(profile_dir, "README.md")
    
    # If the URL is just a github repo URL, try to point to raw main README
    if "github.com" in url and "raw.githubusercontent.com" not in url:
        # e.g., https://github.com/Aradotso/.github
        parsed = urlparse(url)
        path_parts = [p for p in parsed.path.split('/') if p]
        if len(path_parts) >= 2:
            org, repo = path_parts[0], path_parts[1]
            url = f"https://raw.githubusercontent.com/{org}/{repo}/main/profile/README.md"
            print(f"Re-mapped GitHub URL to raw address: {url}")

    success = download_file(url, readme_dest)
    if not success:
        return False

    # Extract images from the newly downloaded README and try to fetch them relative to the README URL
    with open(readme_dest, 'r', encoding='utf-8') as f:
        content = f.read()

    md_images = re.findall(r'!\[(.*?)\]\((.*?)\)', content)
    html_img_tags = re.findall(r'<img\s+[^>]*src=["\'](.*?)["\'][^>]*>', content, re.IGNORECASE)
    
    all_srcs = [src.strip() for _, src in md_images] + [src.strip() for src in html_img_tags]
    
    for src in all_srcs:
        if src.startswith("http://") or src.startswith("https://"):
            continue # Already absolute remote path
            
        # It's a relative path. Let's try downloading it relative to the README's base URL
        base_url = url.rsplit('/', 1)[0] + '/'
        img_url = urljoin(base_url, src)
        dest_img_path = os.path.join(profile_dir, os.path.basename(src))
        
        # Download the image
        download_file(img_url, dest_img_path)

    return True

def main():
    parser = argparse.ArgumentParser(description="Sync profile content from canonical sources.")
    parser.add_argument("--source", help="Path to local directory, README.md, or URL.")
    parser.add_argument("--dir", default="profile", help="Output directory for profile contents.")
    parser.add_argument("--skip-optimize", action="store_true", help="Skip image optimization after sync.")
    parser.add_argument("--skip-validate", action="store_true", help="Skip verification after sync.")
    
    args = parser.parse_args()
    
    if not args.source:
        print("No sync source specified. Use --source <path|url>.")
        print("Example: --source /Users/sve/my-website")
        print("Example: --source https://github.com/Aradotso/.github")
        sys.exit(1)

    os.makedirs(args.dir, exist_ok=True)
    
    # Check if local or remote
    if args.source.startswith("http://") or args.source.startswith("https://"):
        success = sync_from_url(args.source, args.dir)
    else:
        if not os.path.exists(args.source):
            print(f"Error: Local source path '{args.source}' does not exist.")
            sys.exit(1)
        success = sync_from_local(args.source, args.dir)
        
    if not success:
        print("Sync failed!")
        sys.exit(1)
        
    print("\nSync completed successfully!")
    
    # Run optimizer
    if not args.skip_optimize:
        print("\n--- Running Automated Image Optimization ---")
        for filename in os.listdir(args.dir):
            filepath = os.path.join(args.dir, filename)
            ext = filename.lower().split('.')[-1]
            if ext in ('png', 'jpg', 'jpeg', 'webp'):
                max_width = 512 if 'logo' in filename.lower() else 1280
                optimize_image(filepath, max_width=max_width)

    # Run validator
    if not args.skip_validate:
        print("\n--- Running Profile Validation ---")
        is_valid = validate_profile(profile_dir=args.dir)
        if not is_valid:
            print("\nValidation failed for synced profile!")
            sys.exit(1)

if __name__ == "__main__":
    main()
