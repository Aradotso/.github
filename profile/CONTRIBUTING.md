# Contributing to Ara

Thank you for your interest in contributing to Ara! 

As an organization, we build agents that run locally on macOS and automate tasks on your real desktop. 

## Profile Repository

This repository holds the public profile information and assets for the Aradotso organization.

- `profile/README.md`: The public readme displayed on our organization profile.
- `profile/hero.png`: The main hero image.
- `profile/logo.png`: The Ara logo.

## How to update the Organization Profile

To update this profile or add new assets, please follow our draft PR workflow:

1. Create a topic branch from `main`.
2. Make your edits or add new assets under the `profile/` folder.
3. Commit your changes with a descriptive prefix (e.g., `profile: add contributing guidelines`).
4. Push your topic branch to the remote repository.
5. Create a Draft Pull Request using the GitHub CLI: `gh pr create --draft`.
6. Once reviews are complete and checks pass, the PR can be merged.

## Asset Requirements

- **Hero Image**: Maximum width of 1200px. Standard display files should be compressed and under 500KB.
- **Logos & Icons**: Sized appropriately and under 100KB.
- **Paths**: Always use relative paths (e.g., `./hero.png`) to ensure assets load correctly on GitHub.
