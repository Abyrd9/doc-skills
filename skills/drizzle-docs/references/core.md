# Core Drizzle Docs Map

Open the relevant official docs live before implementation.

## Orientation

- https://orm.drizzle.team/docs/overview - Drizzle overview and philosophy: SQL-like TypeScript ORM with both SQL-style and relational query APIs.
- https://orm.drizzle.team/docs/get-started - Setup entry point by database. Use only the native PostgreSQL/MySQL/SQLite paths unless the user asks for a provider.
- https://orm.drizzle.team/docs/connect-overview - Generic database connection concepts before selecting a dialect driver.

## Schema And Relations

- https://orm.drizzle.team/docs/sql-schema-declaration - Core schema declaration, schema files as TypeScript source of truth, table definitions, indexes, enums, casing, and migration source.
- https://orm.drizzle.team/docs/relations-schema-declaration - Application-level relations metadata for relational queries; distinct from SQL foreign key constraints.
- https://orm.drizzle.team/docs/indexes-constraints - Primary keys, foreign keys, unique constraints, checks, indexes, and composite constraints.
- https://orm.drizzle.team/docs/views - SQL views and materialized views where supported.
- https://orm.drizzle.team/docs/custom-types - Custom column types and driver data conversion.
- https://orm.drizzle.team/docs/generated-columns - Generated column declarations and dialect-specific support.

## Querying

- https://orm.drizzle.team/docs/data-querying - Query data overview and entry point for Drizzle’s query APIs.
- https://orm.drizzle.team/docs/rqb-v2 - Relational Query Builder v2 for nested relational fetches.
- https://orm.drizzle.team/docs/select - SQL-like typed select API.
- https://orm.drizzle.team/docs/insert - Insert API and dialect-specific returning/upsert behavior.
- https://orm.drizzle.team/docs/update - Update API.
- https://orm.drizzle.team/docs/delete - Delete API.
- https://orm.drizzle.team/docs/operators - Filter and conditional operators such as `eq`, `and`, `or`, comparisons, null checks, and array helpers where supported.
- https://orm.drizzle.team/docs/joins - Typed join patterns and result shapes.
- https://orm.drizzle.team/docs/sql - Magic `sql`` operator for typed raw expressions and dialect escape hatches.
- https://orm.drizzle.team/docs/transactions - Transactions, nested transactions, savepoints, rollback, and transaction-scoped queries.
- https://orm.drizzle.team/docs/set-operations - Set operations such as `union`, `intersect`, and `except` where supported.
- https://orm.drizzle.team/docs/dynamic-query-building - Dynamic query builder patterns.

## Drizzle Kit And Migrations

- https://orm.drizzle.team/docs/migrations - Migration strategy overview.
- https://orm.drizzle.team/docs/kit-overview - Drizzle Kit command overview.
- https://orm.drizzle.team/docs/drizzle-config-file - `drizzle.config.ts` reference.
- https://orm.drizzle.team/docs/drizzle-kit-generate - Generate SQL migrations from schema diffs.
- https://orm.drizzle.team/docs/drizzle-kit-migrate - Apply generated migrations.
- https://orm.drizzle.team/docs/drizzle-kit-push - Push schema changes directly to a database.
- https://orm.drizzle.team/docs/drizzle-kit-pull - Introspect an existing database into Drizzle schema.
- https://orm.drizzle.team/docs/drizzle-kit-check - Check generated migrations.
- https://orm.drizzle.team/docs/drizzle-kit-studio - Drizzle Studio command reference.
- https://orm.drizzle.team/docs/kit-custom-migrations - Custom migration patterns.
- https://orm.drizzle.team/docs/kit-migrations-for-teams - Team migration workflow guidance.
