#!/usr/bin/env python3
import os
import sys
import argparse
from PIL import Image

def optimize_image(filepath, max_width=None, quality=85):
    """
    Optimizes an image:
    1. Ensures sRGB color space.
    2. Resizes if width exceeds max_width.
    3. Saves with optimization / compression.
    """
    if not os.path.exists(filepath):
        print(f"Error: File {filepath} does not exist.")
        return False

    orig_size = os.path.getsize(filepath)
    try:
        with Image.open(filepath) as img:
            # Check format
            img_format = img.format
            if not img_format:
                print(f"Skipping {filepath}: Unknown format")
                return False

            # Convert to RGB/RGBA sRGB color space
            if img.mode not in ('RGB', 'RGBA'):
                img = img.convert('RGBA' if 'transparency' in img.info or img.mode == 'LA' else 'RGB')

            # Resize if needed
            width, height = img.size
            if max_width and width > max_width:
                aspect_ratio = height / width
                new_width = max_width
                new_height = int(new_width * aspect_ratio)
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                print(f"Resized {filepath} from {width}x{height} to {new_width}x{new_height}")

            # Save with optimization
            temp_path = filepath + ".tmp"
            if img_format == 'PNG':
                img.save(temp_path, format='PNG', optimize=True)
            elif img_format in ('JPEG', 'JPG'):
                img.save(temp_path, format='JPEG', quality=quality, optimize=True)
            elif img_format == 'WEBP':
                img.save(temp_path, format='WEBP', quality=quality)
            else:
                img.save(temp_path, format=img_format)

            new_size = os.path.getsize(temp_path)
            if new_size < orig_size:
                os.replace(temp_path, filepath)
                reduction = (orig_size - new_size) / orig_size * 100
                print(f"Optimized {filepath}: {orig_size/1024:.1f}KB -> {new_size/1024:.1f}KB ({reduction:.1f}% reduction)")
                return True
            else:
                os.remove(temp_path)
                print(f"Kept original {filepath} (no size improvement: {orig_size/1024:.1f}KB)")
                return False

    except Exception as e:
        print(f"Error optimizing {filepath}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Optimize profile branding images.")
    parser.add_argument("--dir", default="profile", help="Directory containing profile images.")
    parser.add_argument("--max-hero-width", type=int, default=1280, help="Max width for hero image.")
    parser.add_argument("--max-logo-width", type=int, default=512, help="Max width for logo image.")
    parser.add_argument("--quality", type=int, default=85, help="Image quality (for lossy formats).")
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.dir):
        print(f"Error: Directory {args.dir} not found.")
        sys.exit(1)
        
    for filename in os.listdir(args.dir):
        filepath = os.path.join(args.dir, filename)
        if not os.path.isfile(filepath):
            continue
            
        ext = filename.lower().split('.')[-1]
        if ext in ('png', 'jpg', 'jpeg', 'webp'):
            max_width = args.max_logo_width if 'logo' in filename.lower() else args.max_hero_width
            optimize_image(filepath, max_width=max_width, quality=args.quality)

if __name__ == "__main__":
    main()
