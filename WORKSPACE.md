# Ara Workspace

This monorepo is managed with [pnpm workspaces](https://pnpm.io/workspaces).
All packages live under `packages/` and all deployable apps live under `apps/`.

## Dependency Rules

Internal packages use the `workspace:*` protocol so pnpm resolves them from
source during development.

### @ara/types

No internal dependencies. This is the foundational type package that everything
else may depend on. It must never import from any other `@ara/*` package.

### @ara/ui

Depends on `@ara/types` only. UI components may use shared types but must not
depend on business-logic packages such as `@ara/api-client`.

### @ara/api-client

Depends on `@ara/types` only. The fetch wrapper uses shared types for request
and response shapes but must not depend on `@ara/ui` or any app package.

### apps/* (@ara/web, @ara/admin, …)

Apps may depend on any package under `packages/*`. No circular dependencies are
allowed — apps must never be imported by packages.

## Allowed Dependency Graph

```
@ara/types   (no internal deps)
     ↑
@ara/ui      ←─ @ara/types
@ara/api-client ←─ @ara/types

apps/web     ←─ @ara/types, @ara/ui, @ara/api-client
apps/admin   ←─ @ara/types, @ara/ui, @ara/api-client
```

## Adding a New Package

1. Create `packages/<name>/` with a `package.json`, `tsconfig.json`, and `src/index.ts`.
2. Name it `@ara/<name>` and set `"private": true`.
3. Add a project reference in the root `tsconfig.json`.
4. Follow the dependency rules above — if you only need types, depend on `@ara/types` only.

## Commands

```bash
# Install all workspace dependencies
pnpm install

# Run a script in every package/app
pnpm -r <script>

# Run a script in a specific workspace
pnpm --filter @ara/types <script>
```
