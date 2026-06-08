# Aradotso Contributor Guide

Welcome! This guide outlines how we develop, build, run, and refine automation at Aradotso. We prioritize high decisiveness, headless execution, and precise, atomic progress.

## Code of Conduct

We are committed to a respectful, productive, and inclusive environment. Collaborate with clarity, support your peers, and focus on delivering robust, high-quality automation.

## Development Setup

To work on Aradotso projects:

1. Clone the repository or use a git worktree.
2. Install dependencies: Use package managers with standard locks (e.g., `npm install`, `pnpm install`, or `pip install -r requirements.txt`). Ensure standard runtimes match the production spec.
3. Verify toolsets: Check your local environment for active CLI tools (`gh`, `vercel`, `stripe`, or `supabase` as appropriate).

## PR Workflow

Our continuous integration and developer workflows are built around isolated, automated environments:

- **Headless Background Worktrees**: We heavily leverage fully automated background agents operating within isolated git worktrees. This allows for safe, parallel experimentation without mutating the main branch or manual workspaces.
- **Draft PRs via GitHub CLI**: Always push your changes to your remote branch and publish your work as a draft pull request. Use the GitHub CLI `gh pr create --draft` to automate this.
- **Decisiveness**: Do not wait for manual intermediate approvals on routine updates. Implement complete, solid changes, run verification suites locally, and commit with clear context.

## Commit Message Conventions

We enforce atomic, descriptive commit messages to maintain a clean git history. Group modifications by folder prefixes to make large codebases easily navigable:

- Use clear structural prefixes:
  - `profile: update brand elements`
  - `devops: tune build triggers`
  - `docs: clarify setup steps`
- Describe what changed and why, keeping the subject line short (under 50 characters).
- Commit early and often during background work to isolate incremental changes.

## Testing Requirements

Every contribution must be verified before merging:

- Run local verification commands depending on the project stack (`npm test`, `pytest`, or custom verification scripts).
- Never assume external API dependencies are active during continuous integration; mock external calls where appropriate.
- Ensure any added scripts are fully non-interactive (use `-y`, `--yes`, or `--non-interactive` flags) so background runners do not hang.

## Review Process

Once a draft PR is published:

1. Automated checks will run in the CI pipeline to verify builds and test suites.
2. Peers or review bots will examine code readability, architectural alignment, and correctness.
3. Upon approval, squash-merge the branch into `main` to keep the main history clean and linear.
