# Aradotso Organization Workflow Templates

This directory contains reusable GitHub Actions workflow templates that are shared across all repositories in the Aradotso organization.

By centralizing these templates here in the `.github` / `amp` organization repository, developers can easily initialize standard CI/CD configurations in any organization repository.

## Available Templates

### 1. Node.js CI (`node-ci.yml`)
Standard CI workflow for Node.js projects. It automates:
- Dependency installation (supporting npm, yarn, and pnpm lockfiles).
- Code linting (runs `npm run lint` or equivalent if configured).
- Running tests (runs `npm run test` or equivalent if configured).
- Running builds (runs `npm run build` or equivalent if configured).
- Supports a multi-version testing matrix (Node.js 18.x, 20.x, and 22.x).

---

## How Repositories Opt-In / Inherit These Templates

GitHub surfaces these organization workflow templates dynamically to any repository in the Aradotso organization.

### Option A: Using the GitHub UI (Recommended)
1. Navigate to your target repository on GitHub.
2. Click on the **Actions** tab.
3. Click **New workflow**.
4. Scroll down or search for the "Templates created by Aradotso" section.
5. Click **Configure** under **Node.js CI**.
6. GitHub will create a local copy of the workflow under `.github/workflows/node-ci.yml` in your target repository.
7. Commit the file to enable the workflow.

### Option B: Direct Copy/Paste
If you prefer to configure manually, you can copy the contents of `node-ci.yml` from this repository directly into `.github/workflows/node-ci.yml` in your target repository.
