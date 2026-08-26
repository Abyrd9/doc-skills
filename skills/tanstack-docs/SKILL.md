---
name: tanstack-docs
description: TanStack guidance for any TanStack library, ecosystem add-on, or app scaffolding work. Load first-party skills shipped with the installed package through TanStack Intent first, then use TanStack CLI JSON docs search for gaps; do not configure the removed `@tanstack/cli mcp` server.
---

# TanStack Docs

Use first-party skills shipped with the installed package as the default source for TanStack work. Use TanStack CLI docs search for exact APIs or packages that do not ship a matching skill.

## Workflow

1. Inspect installed `@tanstack/*` packages and run `bunx @tanstack/intent@latest list --json`.
2. If the installed package ships a matching skill and project policy permits it, load it with `bunx @tanstack/intent@latest load <package>#<skill>` before proposing code.
3. If no matching package skill exists or an exact API claim remains, choose the matching TanStack CLI JSON command below.
4. Provide TanStack-native patterns and commands first.
5. Completion: guidance is grounded in the installed package skill and any needed CLI JSON output, or the answer states why neither could be loaded and keeps the recommendation provisional.

## Detect TanStack context

Treat these as triggers:

- User mentions `tanstack`, `react-query`, `@tanstack/*`, or any named TanStack library.
- The task asks for route/data-loading/state-table patterns that likely map to TanStack libraries.
- The task asks for scaffolding or add-ons in TanStack projects.

## Intent and CLI behavior

- Intent scans static skill files without importing package code. Respect `package.json#intent.skills` and `intent.exclude`; do not widen the allowlist without the user's approval.
- Prefer package-local skills because they version with the installed library.
- Use `bunx @tanstack/intent@latest list --json` for discovery and `bunx @tanstack/intent@latest load <package>#<skill>` for the selected skill.

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
