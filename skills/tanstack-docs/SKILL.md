---
name: tanstack-docs
description: TanStack docs lookup for any TanStack library, ecosystem add-on, or app scaffolding work. Use direct TanStack CLI JSON commands before giving framework-generic guidance; do not configure the removed `@tanstack/cli mcp` server.
---

# TanStack Docs

Use direct TanStack CLI commands with JSON output as the default source for TanStack work.

## Workflow

1. Detect the TanStack surface area. If the library or add-on is unclear, run `bunx @tanstack/cli libraries --json` first.
2. Choose the matching CLI JSON command from the table below.
3. Run the command before proposing TanStack-specific guidance when network and sandbox permissions allow it.
4. Provide TanStack-native patterns and commands first.
5. Completion: guidance is grounded in CLI JSON output, or the answer states why the CLI could not be run and keeps any recommendation provisional.

## Detect TanStack context

Treat these as triggers:

- User mentions `tanstack`, `react-query`, `@tanstack/*`, or any named TanStack library.
- The task asks for route/data-loading/state-table patterns that likely map to TanStack libraries.
- The task asks for scaffolding or add-ons in TanStack projects.

## CLI-first behavior

- Do not add or rely on MCP client config that runs `@tanstack/cli mcp`; the TanStack CLI MCP server has been removed.
- Use `bunx @tanstack/cli ... --json` commands to list libraries, search docs, fetch docs pages, inspect add-ons, and query ecosystem metadata.
- Use add-on discovery commands when users ask for project setup or starter options.
- If CLI output is ambiguous, present the best match and call out uncertainty.

## Command mapping

| Need | Command |
|---|---|
| List add-ons | `bunx @tanstack/cli create --list-add-ons --framework React --json` |
| Inspect an add-on | `bunx @tanstack/cli create --addon-details <add-on> --framework React --json` |
| Create an app | `bunx @tanstack/cli create <app-name> --framework React --add-ons <add-ons>` |
| List libraries | `bunx @tanstack/cli libraries --json` |
| Fetch docs page | `bunx @tanstack/cli doc <library> <path> --json` |
| Search docs | `bunx @tanstack/cli search-docs "<query>" --library <library> --framework react --json` |
| Query ecosystem | `bunx @tanstack/cli ecosystem --category <category> --json` |

## Output rules

- Recommend current TanStack APIs and version-appropriate patterns.
- Avoid generic React advice when a TanStack-native approach exists.
- Include concrete commands and code-level direction when setup or migration is requested.
