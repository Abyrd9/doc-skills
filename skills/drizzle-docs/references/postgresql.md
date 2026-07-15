# Native PostgreSQL Drizzle Docs Map

Use these pages for native PostgreSQL only. Avoid Neon, Supabase, Vercel Postgres, Prisma Postgres, Xata, Nile, PlanetScale Postgres, PGLite, AWS Data API, and other provider pages unless requested.

## Connection

- https://orm.drizzle.team/docs/get-started-postgresql - Native PostgreSQL setup with `node-postgres` and `postgres.js`, connection strings, config objects, and existing clients.
- https://orm.drizzle.team/docs/connect-overview - Generic connection concepts.

## Schema And `pg-core`

- https://orm.drizzle.team/docs/sql-schema-declaration - `pgTable`, schema source of truth, casing, PostgreSQL schemas/sequences/enums/views/materialized views.
- https://orm.drizzle.team/docs/column-types/pg - PostgreSQL column types from `drizzle-orm/pg-core`: integer families, serials, identity, boolean, bytea, text/varchar/char, numeric, floats, json/jsonb, uuid, date/time/timestamp/interval, point/line, arrays, defaults, nullability, primary keys.
- https://orm.drizzle.team/docs/column-types/pg#enum - `pgEnum` and PostgreSQL enum generation.
- https://orm.drizzle.team/docs/indexes-constraints - PostgreSQL indexes and constraints, including `index`, `uniqueIndex`, `.concurrently()`, partial indexes, operator classes, and storage parameters.
- https://orm.drizzle.team/docs/sequences - `pgSequence` and PostgreSQL sequence options.
- https://orm.drizzle.team/docs/views - `pgView`, `pgMaterializedView`, query builder/raw SQL views, and materialized view refresh.
- https://orm.drizzle.team/docs/schemas - PostgreSQL schema declarations.
- https://orm.drizzle.team/docs/custom-types - PostgreSQL custom type mapping.

## Migrations And Config

- https://orm.drizzle.team/docs/drizzle-config-file - Use `dialect: "postgresql"` and native PostgreSQL credentials. Check migration table/schema settings, schema filters, extension filters, roles, strict/verbose, and breakpoints.
- https://orm.drizzle.team/docs/drizzle-kit-generate - Generate PostgreSQL migrations.
- https://orm.drizzle.team/docs/drizzle-kit-migrate - Apply PostgreSQL migrations.
- https://orm.drizzle.team/docs/drizzle-kit-push - Push PostgreSQL schema changes directly.
- https://orm.drizzle.team/docs/drizzle-kit-pull - Introspect PostgreSQL schema.

## PostgreSQL Query Patterns

- https://orm.drizzle.team/docs/select - Selects, CTEs, subqueries, aggregation, pagination, iterators, and raw SQL for unsupported features.
- https://orm.drizzle.team/docs/insert - PostgreSQL `.returning()`, conflict handling, `onConflictDoNothing`, `onConflictDoUpdate`, composite conflict targets, and CTE-backed inserts.
- https://orm.drizzle.team/docs/update - PostgreSQL `.returning()`, CTE-backed updates, and `UPDATE ... FROM`.
- https://orm.drizzle.team/docs/operators - Operators including PostgreSQL array helpers.
- https://orm.drizzle.team/docs/joins - Typed joins.
- https://orm.drizzle.team/docs/sql - Typed raw SQL fragments and `.mapWith()`.
- https://orm.drizzle.team/docs/set-operations - PostgreSQL set operations from `drizzle-orm/pg-core`.
- https://orm.drizzle.team/docs/transactions - Transactions and savepoints.
- https://orm.drizzle.team/docs/rqb-v2 - Relational Query Builder v2 for PostgreSQL and other dialects.

