# Contributing to Aradotso

Thanks for your interest in contributing to the Aradotso GitHub org profile and its shared tooling.

## Proposing Changes

Open a pull request against `main`. Branch names should be descriptive and kebab-cased (e.g. `update-org-readme`, `add-issue-template`). Every PR needs at least one approving review from an Aradotso maintainer before merge. For large structural changes, open an issue first to align on direction.

## What Lives Here

This repository is for org-level assets only:

- `profile/` — org profile page README and image assets
- `branding/` — canonical logo exports, color tokens, brand guide
- `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md` — community health files
- `CHANGELOG.md` — record of notable changes

For contributions to specific Ara products (AraDesktop, AraWeb, etc.), see the relevant repository.

## Coding Standards

For any org-level tools, templates, or automation scripts:

- Prefer TypeScript or shell scripts; keep dependencies minimal.
- Scripts must be idempotent where possible.
- Add a short comment block at the top of each file describing its purpose.
- Format code with Prettier (TypeScript) or `shfmt` (shell) before committing.

## Commit Message Conventions

Use a folder prefix that identifies which part of the org is affected:

- `(OrgProfile) update hero image`
- `(Branding) add dark logo variant`
- `(CI) fix release workflow`

Keep the subject line under 72 characters. Add a body if the why is not obvious.

## Changelog

Update `CHANGELOG.md` under `[Unreleased]` with a brief entry for every PR that changes a user-visible file.

## License and CLA

All contributions are made under the repository's existing license. By opening a PR you confirm that you have the right to submit the work and agree to license it accordingly.

## Reporting Security Issues

Do not open a public issue for security vulnerabilities. Email **security@ara.so** directly. See `SECURITY.md` for full details.
