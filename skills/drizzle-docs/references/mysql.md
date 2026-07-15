# Native MySQL Drizzle Docs Map

Use these pages for native MySQL only. Avoid PlanetScale, SingleStore, AWS Data API MySQL, TiDB, and other provider/vendor pages unless requested.

## Connection

- https://orm.drizzle.team/docs/get-started-mysql - Native MySQL setup with `mysql2`; imports from `drizzle-orm/mysql2`; supports URLs, mysql2 connection options, existing connections, and pools. Use a single client connection for DDL migrations.
- https://orm.drizzle.team/docs/connect-overview - Generic connection concepts.

## Schema And `mysql-core`

- https://orm.drizzle.team/docs/column-types/mysql - MySQL column types from `drizzle-orm/mysql-core`: numeric types, `serial`, binary/blob, char/varchar/text, boolean, date/time, json, `mysqlEnum`, `$type`, `.default`, `$defaultFn`, `$onUpdate`, primary keys, and autoincrement.
- https://orm.drizzle.team/docs/sql-schema-declaration - `mysqlTable`, `mysqlSchema`, `AnyMySqlColumn`, `mysqlEnum`, indexes, self references, and schema source of truth. Remember that MySQL schema maps to database and is not detected/included by Drizzle Kit migrations.
- https://orm.drizzle.team/docs/indexes-constraints - MySQL defaults, not-null, unique/composite unique, checks, primary keys, foreign keys, self references, multi-column foreign keys, indexes, and MySQL index options such as `.algorithm()`, `.lock()`, and `.using()`.
- https://orm.drizzle.team/docs/generated-columns - MySQL generated columns with `STORED` and `VIRTUAL`, index support, constraints, and `.generatedAlwaysAs(..., { mode })`.
- https://orm.drizzle.team/docs/custom-types - Custom column type mapping.

## Migrations And Config

- https://orm.drizzle.team/docs/drizzle-config-file - Use `dialect: "mysql"` and native MySQL credentials via URL or host/port/user/password/database/ssl. Treat `driver` examples as exception/vendor cases unless needed.
- https://orm.drizzle.team/docs/drizzle-kit-generate - Generate MySQL migrations.
- https://orm.drizzle.team/docs/drizzle-kit-migrate - Apply MySQL migrations and track history.
- https://orm.drizzle.team/docs/drizzle-kit-push - Push MySQL schema changes directly.
- https://orm.drizzle.team/docs/drizzle-kit-pull - Introspect MySQL schema.

## MySQL Query Patterns

- https://orm.drizzle.team/docs/select - SQL-like selects, iterator support, and MySQL index hints such as `useIndex`, `ignoreIndex`, and `forceIndex`.
- https://orm.drizzle.team/docs/insert - MySQL insert conflict handling via `onDuplicateKeyUpdate`.
- https://orm.drizzle.team/docs/update - Update API.
- https://orm.drizzle.team/docs/delete - Delete API.
- https://orm.drizzle.team/docs/operators - Filters and conditional operators.
- https://orm.drizzle.team/docs/joins - Typed joins.
- https://orm.drizzle.team/docs/sql - Typed raw SQL fragments and escape hatches.
- https://orm.drizzle.team/docs/transactions - Transactions.
- https://orm.drizzle.team/docs/rqb-v2 - Relational Query Builder v2 for MySQL and other dialects.

