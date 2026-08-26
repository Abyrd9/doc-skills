---
name: effect-docs
description: Effect official-docs workflow for TypeScript code using Effect, Schema, services, Layers, typed errors, resource management, concurrency, streams, scheduling, configuration, observability, testing, Micro, AI, or @effect/platform packages. Use before implementing, debugging, migrating, or reviewing Effect-specific APIs and patterns.
---

# Effect Docs

Use current official Effect documentation and the project's installed package surface as the sources of truth.

## 1. Establish local context

1. Inspect `package.json` and the lockfile for `effect` and `@effect/*` packages, including exact versions and prerelease tags.
2. Inspect Effect imports, `tsconfig.json`, runtime, package manager, tests, and existing composition style.
3. Identify the relevant surface: core Effect, errors, services and Layers, resources, concurrency, Stream or Sink, Schema, Platform, AI, Micro, or another module.

Do not apply current examples blindly to an older installed version. Do not introduce an unstable surface unless the project already uses it or the user explicitly asks for it.

Completion criterion: the documentation search is scoped to the installed versions, runtime, imports, and Effect surface involved in the task.

## 2. Route through official docs

1. If the installed `effect` package contains `node_modules/effect/AGENTS.md`, read it completely first. It is first-party guidance shipped with that exact package version.
2. Open `https://effect.website/docs/` and the smallest set of matching official pages.
3. Use the API reference linked from the official docs when an exact signature, overload, export, or package boundary matters.

Common branches:

- Fundamentals: installation, importing, the Effect type, creating and running Effects, generators, pipelines, and control flow.
- Failures: expected errors, defects, `Cause`, recovery, retries, timeouts, and accumulation.
- Dependencies and lifetime: services, Layers, Scope, resource acquisition, and finalization.
- Runtime behavior: concurrency, fibers, queues, scheduling, state, caching, batching, Stream, and Sink.
- Data boundaries: Schema decoding and encoding, transformations, filters, error formatting, and generated representations.
- Applications: configuration, logging, metrics, tracing, testing, and the matching Platform runtime.
- Style or migration: code-style pages and the relevant comparison or migration guide.
- Unstable modules: read the module introduction and exact feature page, then preserve the instability warning in the recommendation.

Completion criterion: every Effect-specific API, import, type parameter, or runtime claim is covered by a fetched official page for the relevant installed surface.

For deeper pattern guidance, use [references/docs-index.md](references/docs-index.md) to select one bundled guide. Treat these guides as secondary to installed package types and current official docs.

## 3. Fit the docs to the codebase

- Preserve the project's import style, generator or pipeline style, service conventions, runtime adapter, and testing setup unless the task changes them.
- Prefer inferred and package-provided types over handwritten equivalents or casts.
- Keep expected errors, defects, and interruption distinct; consult the matching error pages before changing error channels.
- Compose Effects before running them, and use the documented platform entry point at the application boundary when graceful teardown matters.
- Use Scope and resource-management APIs for lifetimes that must remain safe under failure or interruption.
- Check both service and Layer guidance before changing dependency construction or provisioning.
- If current docs disagree with the installed version, inspect installed types or source and official release notes, then state the mismatch.

Completion criterion: the implementation matches both official guidance and the project's established Effect version and conventions.

## 4. Verify

Run the repository's smallest relevant checks: typecheck, focused tests, and its configured Effect language-service or lint checks. Use `TestClock` or the documented test utility for time-dependent Effect behavior instead of real waiting when applicable.

Report the official pages used, installed Effect versions that shaped the answer, checks run, and unresolved assumptions.

## Source fallback order

1. The installed package's `AGENTS.md`, when present, and the matching official guide pages.
2. The API references linked from `https://effect.website/docs/additional-resources/api-reference/`.
3. Installed package types or source for the pinned version.
4. Official Effect repository material or release notes for remaining version-specific gaps.

Do not use third-party examples to override official docs or the installed package surface.
