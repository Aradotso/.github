# Ara Public Profile Repository (.github)

This repository contains the public branding layout and GitHub profile assets for the Ara organization.

## Repository Structure

- `profile/`: Contains the public profile information.
  - `README.md`: The main profile page displayed on the Ara organization page.
  - `logo.png`: Main logo asset.
  - `hero.png`: Profile banner / hero asset.
- `scripts/`: Tooling for maintaining, optimizing, and synchronizing profile content.
  - `sync_profile.py`: Core CLI script to sync profile information from local and remote canonical sources.
  - `optimize_images.py`: Automated asset optimization and scaling script ensuring standard formats, dimensions, sRGB profiles, and optimized file sizes.
  - `validate_profile.py`: A verification test checking image integrity, relative paths, case-sensitivity matching, alt descriptions, and standard formatting guidelines.

## Development & Maintenance

This repository includes fully automated validation and synchronization tools.

### 1. Validate Profile Integrity
To verify that the profile markdown and assets render correctly on GitHub without any broken relative paths or rendering issues:
```bash
python3 scripts/validate_profile.py
```

### 2. Optimize Branding Images
To automatically compress, resize, and optimize png/jpg assets in the profile directory:
```bash
python3 scripts/optimize_images.py
```

### 3. Synchronize Profile
To sync profile information and branding assets from a local folder or a remote URL, and automatically optimize and validate them:
```bash
python3 scripts/sync_profile.py --source /path/to/canonical-source
# OR
python3 scripts/sync_profile.py --source https://github.com/Aradotso/some-source-repo
```

## Continuous Integration

A GitHub Actions CI workflow (`.github/workflows/profile-ci.yml`) is set up to automatically optimize images and validate profile integrity on every push and pull request to the `main` branch.
