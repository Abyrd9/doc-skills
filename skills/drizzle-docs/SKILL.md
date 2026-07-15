---
name: drizzle-docs
description: "Drizzle docs workflow for Drizzle ORM and drizzle-kit work: schemas, queries, migrations, Drizzle Kit config, dialect imports, relations, transactions, raw SQL, indexes, constraints, and native PostgreSQL/MySQL/SQLite. Avoid provider-specific docs unless requested."
---

# Drizzle Docs

## Source Policy

Use official Drizzle docs first: `https://orm.drizzle.team/docs/...`.

Avoid provider-specific pages unless the user explicitly asks for them. This skill supports native Drizzle docs for:

- Core Drizzle ORM and Drizzle Kit.
- Native PostgreSQL.
- Native MySQL.
- Native/local SQLite.

Skip provider/runtime pages by default, including Neon, Supabase, Vercel Postgres, PlanetScale, TiDB, SingleStore, AWS Data API, Turso Cloud, SQLite Cloud, Cloudflare D1, Durable Objects, Expo SQLite, OP SQLite, and React Native SQLite.

## Core Workflow

1. Identify the task lane:
   - General schema/query/migration work -> [references/core.md](references/core.md).
   - PostgreSQL -> [references/postgresql.md](references/postgresql.md).
   - MySQL -> [references/mysql.md](references/mysql.md).
   - SQLite -> [references/sqlite.md](references/sqlite.md).
2. Open the relevant official docs live before giving detailed guidance or editing code.
3. Match imports to the dialect:
   - PostgreSQL: `drizzle-orm/pg-core`.
   - MySQL: `drizzle-orm/mysql-core`.
   - SQLite: `drizzle-orm/sqlite-core`.
4. Match the runtime driver to native docs:
   - PostgreSQL: `node-postgres` or `postgres.js`.
   - MySQL: `mysql2`.
   - SQLite: `node:sqlite`, `bun:sqlite`, or `better-sqlite3` unless the project already uses another supported native/local option.
5. Check `drizzle.config.ts` against the docs for the selected dialect before running or changing migrations.
6. Prefer Drizzle’s SQL-like APIs for straightforward queries and relational query builder docs for nested relation loading.
7. Use `sql`` only as an escape hatch for dialect-specific expressions, custom snippets, or unsupported query constructs.
8. Completion: the implementation or answer follows the selected dialect docs, and any provider-specific guidance is either requested by the user or explicitly excluded.

## Migration Guidance

Choose the migration workflow deliberately:

- Use `drizzle-kit generate` plus `drizzle-kit migrate` for source-controlled migrations.
- Use `drizzle-kit push` for rapid prototyping or controlled direct schema sync.
- Use `drizzle-kit pull` for database-first introspection.
- Read `drizzle.config.ts` docs before changing dialect, credentials, schema paths, output paths, casing, migration table/schema, filters, strictness, or verbose settings.

## Review Checklist

When implementing or reviewing Drizzle code:

- Confirm the dialect-specific imports match the database.
- Confirm schema files are exported and included by Drizzle Kit config.
- Confirm relations metadata is not confused with SQL foreign key constraints.
- Confirm migration workflow matches the project’s deployment model.
- Confirm inserts/updates/deletes use dialect-supported returning/upsert behavior.
- Confirm raw SQL fragments are typed where useful and safely parameterized.
- Confirm transactions use the transaction-scoped `tx` object.
- Confirm provider-specific docs are not being followed for native database setups.
