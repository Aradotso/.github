# Contributing to Aradotso

Thank you for contributing to the Aradotso GitHub organization profile! This
repository manages the public appearance of the Aradotso organization on GitHub.

## Getting Started

To set up the development environment and tools locally, make sure you have
[Node.js](https://nodejs.org/) installed (v20+ is recommended).

1. Clone this repository (or checkout your worktree).
2. Install the linting and formatting dependencies:

   ```bash
   make install
   ```

## Development Tooling

We use automated tooling to keep the repository assets and markdown files clean,
consistent, and well-formatted.

### Linting Markdown

To check for style issues or bad links inside any of our markdown documents,
run:

```bash
make lint
```

### Checking and Applying Formatting

We use Prettier to format markdown and JSON files. To check formatting:

```bash
make format
```

To automatically fix formatting:

```bash
make format-write
```

## Adding Branding Assets

Our organization-wide assets live inside the `profile/` directory (e.g.,
`hero.png`, `logo.png`). When adding or updating assets:

- Use clear, descriptive file names.
- Ensure images are optimized for the web (compressed files, high-resolution
  formats).
- Always use relative paths when referencing assets from markdown files (e.g.,
  `./hero.png`) rather than absolute URLs.
