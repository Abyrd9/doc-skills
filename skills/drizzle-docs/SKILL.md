---
name: drizzle-docs
description: Use official Drizzle ORM and Drizzle Kit documentation before implementing, changing, debugging, or reviewing Drizzle code. Covers database and provider connections, schemas, data types, constraints, relations, queries, transactions, raw SQL, migrations, drizzle.config.ts, seeding, validation integrations, extensions, and version upgrades across supported dialects and drivers.
---

# Drizzle Docs

Use the current official Drizzle docs and the project's installed package surface as the sources of truth. Fit the documented approach to the project's existing version, dialect, driver, and migration workflow.

## 1. Establish the local Drizzle context

Before choosing documentation:

1. Inspect `package.json` and the lockfile for `drizzle-orm`, `drizzle-kit`, and related packages such as `drizzle-zod`.
2. Inspect `drizzle.config.*`, schema files, migration folders, and scripts.
3. Search Drizzle imports to identify the dialect, driver, provider, runtime, and query API already in use.
4. Note whether the installed packages are stable, beta, RC, or another prerelease.

Do not route a stable project through prerelease or v1-upgrade guidance unless the user asks to upgrade. If no project context exists, state the assumed dialect, driver, runtime, and release channel before recommending code.

Completion criterion: the documentation search is scoped to the project's actual Drizzle version, dialect, driver or provider, and migration workflow.

## 2. Route through the live documentation index

Start at [Drizzle ORM Docs](https://orm.drizzle.team/docs/overview). Treat that page as the live route map instead of relying on a memorized URL list.

Open the smallest set of pages that covers the task:

- Setup: **Get started**, **Connect**, the exact database or provider page, and `drizzle.config.ts` when Drizzle Kit is involved.
- Schema: schema declaration, the matching dialect's column types, indexes and constraints, generated columns, views, sequences, or row-level security.
- Relations: the relations page plus indexes and constraints when database foreign keys also matter.
- Queries: the exact select, insert, update, delete, filter, join, relational-query, transaction, batch, or `sql` page used by the change.
- Migrations: the workflow overview plus the exact `generate`, `migrate`, `push`, `pull`, or `up` page involved.
- Other features: seeding, validation integrations, extensions, read replicas, caching, or performance guidance only when the task needs them.
- Upgrades: the matching official upgrade page and breaking-change notes, only after confirming the project's release channel and target version.

Use provider-specific instructions when the project uses that provider. Do not silently substitute generic dialect setup for a provider-specific driver, transport, or runtime.

Completion criterion: every Drizzle-specific API, import path, config key, or CLI command in the proposed work is covered by a fetched official page for the relevant setup.

## 3. Apply the docs to the existing codebase

- Preserve the project's package manager, runtime, dialect imports, driver, schema layout, and naming conventions unless the task is explicitly changing them.
- Prefer package-provided and inferred types. Avoid reproducing Drizzle-owned shapes by hand.
- Follow the query style already used locally unless the requested change requires another documented API.
- Read both relations and constraint documentation before assuming application relation metadata and database foreign keys are interchangeable.
- Use Drizzle's documented `sql` escape hatch when needed, and preserve its parameterization behavior.
- Respect the repository's existing migration mode. Do not replace `generate` plus `migrate`, `push`, or `pull` with another workflow as an incidental cleanup.
- Treat `drizzle-kit up` as a version-upgrade operation, not a routine schema-application command.

If current docs and the installed version appear to disagree, inspect the installed package types or source and official release notes. State the version mismatch rather than forcing current examples onto an older API.

Completion criterion: the implementation or recommendation matches both the fetched docs and the codebase's established Drizzle setup.

## 4. Protect database state

- Never infer that a configured database is disposable or safe to mutate.
- Before running a database-touching command, identify the target environment and confirm the user's request authorizes that operation.
- Prefer local generation and inspection when it can verify the change without touching a database.
- Review generated SQL before applying it, especially for drops, renames, backfills, constraints, and type changes.
- Do not run `push`, `migrate`, or another mutating command against production merely to verify an answer.

## 5. Verify the result

Run the repository's relevant checks, usually:

1. Typecheck and focused tests.
2. The existing Drizzle Kit validation or generation command when the task changes schema or config.
3. Inspection of generated SQL or migration output when applicable.
4. A database-backed check only when it is authorized and the target is confirmed.

Report:

- the Drizzle version or release channel, dialect, and driver or provider that shaped the answer;
- the official pages used;
- checks run and their results;
- any unresolved version or environment assumptions.

## Source fallback order

1. Current official Drizzle documentation selected through the overview page.
2. Official Drizzle release notes or repository material for version-specific gaps.
3. Installed package types or source for the project's pinned version.
4. Broader web search only when the official sources do not answer the question.

Do not use third-party examples to override official docs or the installed package surface.
