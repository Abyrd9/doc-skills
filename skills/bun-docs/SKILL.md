---
name: bun-docs
description: Bun docs lookup for Bun runtime, package manager, test, and API work. Use Bun's official sitemap plus route `.md` pages before giving Bun-specific guidance; use MCP only when it is exposed and healthy.
---

# Bun Docs

Use Bun official docs as the first source of truth for Bun tasks.

## Workflow

1. Detect the Bun surface area: runtime API, package manager, test runner, scripts, config, Node compatibility, or project setup.
2. Fetch `https://bun.com/docs/sitemap.xml`.
3. Resolve the smallest set of matching `https://bun.com/docs/...` routes.
4. Fetch the matching `<route>.md` pages, such as `https://bun.com/docs/pm/bunx.md`; if a `.md` route fails, try one nearby route from the sitemap before falling back.
5. Answer from those pages first; fall back to general JavaScript or Node guidance only when Bun docs do not cover the topic.
6. Completion: the answer or code change is grounded in the fetched Bun route, or it explicitly says Bun docs did not cover the needed detail.

## Detect Bun context

Treat these as triggers:

- User says `bun`, `bunx`, `bun test`, `bun run`, `bun install`, or `Bun.js`.
- Files include `bun.lock`, `bunfig.toml`, or scripts that use `bun`.
- The task involves runtime APIs where Bun differs from Node.

## MCP fallback

- If a Bun docs MCP server is exposed in the current tool surface and healthy, it can be used for convenience.
- If MCP fails, continue with sitemap + `.md` fetch and do not block the task.

## Output rules

- Prefer Bun-native commands over Node/NPM equivalents when both are valid.
- Call out compatibility caveats when suggesting libraries or Node-specific features.
- Keep answers implementation-focused and include exact commands when setup is requested.
