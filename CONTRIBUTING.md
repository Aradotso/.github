# Contributing to Aradotso

Thanks for your interest in contributing to the Aradotso GitHub org profile and its shared tooling.

## Proposing Changes

Open a pull request against `main`. Branch names should be descriptive and kebab-cased (e.g. `update-org-readme`, `add-issue-template`). Every PR needs at least one approving review from an Aradotso maintainer before merge. For large structural changes, open an issue first to align on direction.

## Coding Standards

For any org-level tools, templates, or automation scripts:

- Prefer TypeScript or shell scripts; keep dependencies minimal.
- Scripts must be idempotent where possible.
- Add a short comment block at the top of each file describing its purpose.
- Format code with Prettier (TypeScript) or `shfmt` (shell) before committing.

## Commit Message Conventions

Use a folder prefix that identifies which part of the org is affected, matching the convention used across Ara repos:

- `(OrgProfile) update hero image`
- `(Templates) add bug report template`
- `(CI) fix release workflow`

Keep the subject line under 72 characters. Add a body if the why is not obvious.

## License and CLA

All contributions are made under the repository's existing license. By opening a PR you confirm that you have the right to submit the work and agree to license it accordingly. A formal CLA process is not yet in place; this notice acts as a lightweight contributor agreement.

## Reporting Security Issues

Do not open a public issue for security vulnerabilities. Email security@ara.so directly. Include a description of the issue, steps to reproduce, and any relevant context. We aim to acknowledge reports within 48 hours.
