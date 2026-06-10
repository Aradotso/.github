# Org Workflow Templates

These templates are available to all Aradotso repos via the GitHub "Actions" → "New workflow" page.
GitHub discovers them automatically from this `.github` repo and surfaces them under the org section
when creating a new workflow in any Aradotso repository.

## Available Templates

`nodejs-ci` — Lint, test, and build pipeline for Node.js projects. Runs jobs in sequence
(lint → test → build) using Node.js 20 with npm caching. Triggers on push to `main`/`develop`
and on pull requests targeting `main`.

## How to opt in

**Via GitHub UI (recommended):**

1. Navigate to your repository on GitHub.
2. Click the "Actions" tab.
3. Click "New workflow".
4. Under the Aradotso org section, choose "Node.js CI".
5. GitHub will copy the template into `.github/workflows/` in your repo. Commit the file.

**Manually:**

Copy `workflow-templates/nodejs-ci.yml` into your repo's `.github/workflows/` directory,
rename the file if needed, and adjust the `name` field or matrix settings to suit your project.

## Local validation

YAML syntax can be checked before pushing:

```sh
npx js-yaml .github/workflows/your-workflow.yml
# or
yamllint .github/workflows/your-workflow.yml
```

For full GitHub Actions-specific validation (expression syntax, step IDs, runner labels),
[actionlint](https://github.com/rhysd/actionlint) is recommended:

```sh
brew install actionlint   # macOS
actionlint               # run from the repo root
```
