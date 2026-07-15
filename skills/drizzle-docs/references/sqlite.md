# Native SQLite Drizzle Docs Map

Use these pages for native/local SQLite. Avoid Turso Cloud, SQLite Cloud, Cloudflare D1, Durable Objects, Expo SQLite, OP SQLite, and React Native SQLite unless requested. `libsql` can be local-file SQLite-like or remote Turso; prefer `node:sqlite`, `bun:sqlite`, or `better-sqlite3` for native/local Node or Bun projects unless the project already chose libSQL.

## Connection

- https://orm.drizzle.team/docs/get-started-sqlite - Main SQLite setup page covering `libsql`, `node:sqlite`, and `better-sqlite3`.
- https://orm.drizzle.team/docs/connect-node-sqlite - Native Node `node:sqlite` driver with local file connections, existing `DatabaseSync` clients, and sync APIs.
- https://orm.drizzle.team/docs/connect-bun-sqlite - Native Bun `bun:sqlite` driver with local/in-memory SQLite, existing Bun `Database` clients, and sync APIs.
- https://orm.drizzle.team/docs/connect-overview - Generic connection concepts.

## Schema And `sqlite-core`

- https://orm.drizzle.team/docs/column-types/sqlite - SQLite column types from `drizzle-orm/sqlite-core`: `sqliteTable`, `integer`, `real`, `text`, `blob`, `numeric`, modes for booleans, timestamps, JSON, bigint, defaults, `$type()`, and `notNull()`.
- https://orm.drizzle.team/docs/indexes-constraints - SQLite defaults, not-null, unique indexes, check constraints, primary/composite keys, foreign keys, and indexes.
- https://orm.drizzle.team/docs/generated-columns - SQLite generated columns, stored vs virtual modes, and SQLite limitations around altering generated expressions.
- https://orm.drizzle.team/docs/custom-types - Custom column type mapping.

## Migrations And Config

- https://orm.drizzle.team/docs/drizzle-config-file - Use `dialect: "sqlite"` and `dbCredentials.url` as `":memory:"`, `"sqlite.db"`, or `"file:sqlite.db"` when required. Avoid D1-specific `driver: "d1-http"` for native/local SQLite.
- https://orm.drizzle.team/docs/drizzle-kit-generate - Generate SQLite migrations.
- https://orm.drizzle.team/docs/drizzle-kit-migrate - Apply SQLite migrations and track history.
- https://orm.drizzle.team/docs/drizzle-kit-push - Push SQLite schema changes directly; be careful with generated columns and SQLite ALTER limitations.
- https://orm.drizzle.team/docs/drizzle-kit-pull - Introspect SQLite schema.

## SQLite Query Patterns

- https://orm.drizzle.team/docs/select - SQL-like select builder.
- https://orm.drizzle.team/docs/insert - Inserts and conflict handling where supported.
- https://orm.drizzle.team/docs/update - Update API.
- https://orm.drizzle.team/docs/delete - Delete API.
- https://orm.drizzle.team/docs/operators - Filters/operators such as `eq`, `and`, `or`, `inArray`, and `like`.
- https://orm.drizzle.team/docs/joins - Join patterns.
- https://orm.drizzle.team/docs/sql - SQLite-specific raw expressions and custom defaults.
- https://orm.drizzle.team/docs/transactions - Transactions.
- https://orm.drizzle.team/docs/rqb-v2 - Relational Query Builder v2 for SQLite and other dialects.

