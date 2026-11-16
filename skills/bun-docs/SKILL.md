---
name: bun-docs
description: Bun docs lookup for Bun runtime, package manager, test, type checking, formatter, and API work. Use Bun's official LLM index plus route `.md` pages before giving Bun-specific guidance; use MCP only when it is exposed and healthy.
---

# Bun Docs

Use Bun official docs as the first source of truth for Bun tasks.

## Workflow

1. Inspect the project's pinned Bun version or run `bun --version` when available.
2. Detect the Bun surface area: runtime API, package manager, test runner, type checking, formatter, scripts, config, Node compatibility, or project setup.
3. Fetch `https://bun.com/llms.txt`.
4. Resolve the smallest set of matching `https://bun.com/docs/...` routes.
5. Fetch the matching `<route>.md` pages, such as `https://bun.com/docs/pm/bunx.md`; if a `.md` route fails, try one nearby route from the index before falling back.
6. If the index omits a command present in the installed release, check the same-topic official HTML page or site navigation first. For example, `https://bun.com/docs/runtime/check` and `https://bun.com/docs/format` are live but absent from the index.
7. Read that version's official Bun release notes when the live docs do not establish when the command shipped.
8. Answer from those pages first; fall back to general JavaScript or Node guidance only when Bun docs do not cover the topic.
9. Completion: the answer or code change is grounded in a fetched Bun route or release note, or it explicitly says Bun docs did not cover the needed detail.

## Detect Bun context

Treat these as triggers:

- User says `bun`, `bunx`, `bun test`, `bun fmt`, `bun run`, `bun install`, or `Bun.js`.
- Files include `bun.lock`, `bunfig.toml`, or scripts that use `bun`.
- The task involves runtime APIs where Bun differs from Node.

## MCP fallback

- If a Bun docs MCP server is exposed in the current tool surface and healthy, it can be used for convenience.
- If MCP fails, continue with the LLM index + `.md` fetch and do not block the task.

## Output rules

- Prefer Bun-native commands over Node/NPM equivalents when both are valid.
- Call out compatibility caveats when suggesting libraries or Node-specific features.
- Keep answers implementation-focused and include exact commands when setup is requested.
