# Ara Monorepo Workspace

This is a pnpm TypeScript monorepo managed via pnpm workspaces.

## Structure

```
.
├── apps/
│   ├── web/          @ara/web       Next.js web app
│   └── mobile/       @ara/mobile    React mobile/web app
├── packages/
│   ├── types/        @ara/types     Shared TypeScript types
│   ├── ui/           @ara/ui        Shared UI components
│   └── api-client/   @ara/api-client HTTP API client
├── pnpm-workspace.yaml
├── package.json
├── tsconfig.base.json
└── WORKSPACE.md
```

## Dependency Rules

The following rules govern inter-package dependencies. Violating these rules introduces circular dependencies and build-order issues.

### Allowed dependencies

- `@ara/types` — no internal dependencies (foundational package)
- `@ara/ui` — depends on `@ara/types` only
- `@ara/api-client` — depends on `@ara/types` only
- `@ara/web` — depends on `@ara/types`, `@ara/ui`, and optionally `@ara/api-client`
- `@ara/mobile` — depends on `@ara/types`, `@ara/ui`, and optionally `@ara/api-client`

### No circular dependencies

Circular dependencies are strictly forbidden. The dependency graph must remain a directed acyclic graph (DAG):

```
@ara/types
    ↑
@ara/ui    @ara/api-client
    ↑           ↑
      @ara/web / @ara/mobile
```

Never add a dependency from `@ara/types` to any other internal package. Never add a dependency from `@ara/ui` to `@ara/api-client` or any app package.

## Adding a New Package

1. Create a directory under `packages/your-package-name/`.
2. Add a `package.json` with `"name": "@ara/your-package-name"` and `"version": "0.1.0"`.
3. Add a `tsconfig.json` that extends `../../tsconfig.base.json`.
4. Add `src/index.ts` as the package entry point.
5. Declare internal workspace dependencies as `"workspace:*"` in `package.json`.
6. Run `pnpm install` from the repo root to link the new package.
7. Add a path alias for the package in the root `tsconfig.base.json` under `compilerOptions.paths`.
8. Document the package and its allowed dependencies in this file.

## Adding a New App

1. Create a directory under `apps/your-app-name/`.
2. Follow the same steps as adding a package (steps 2–6 above).
3. Apps may depend on any package in `packages/` but packages must never depend on apps.

## Running Commands

```bash
# Install all dependencies
pnpm install

# Build all packages and apps
pnpm build

# Run all dev servers in parallel
pnpm dev

# Type-check the entire workspace
pnpm typecheck

# Run a command in a specific package
pnpm --filter @ara/types build
```
