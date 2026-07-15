---
name: xstate-docs
description: XState docs lookup for state machines, actors, invoked services, guards, actions, context, transitions, React integration, TypeScript typing, testing, and v4-to-v5 migration work. Use Stately canonical docs before giving XState implementation guidance.
---

# XState Docs

Use Stately canonical docs as the source of truth for XState API, pattern, migration, and implementation questions.

## Source Priority

Start from these canonical sources:

- https://stately.ai/llms.txt
- https://stately.ai/llms-full.txt

If another source conflicts with these, prefer the Stately sources and call out the conflict.

## Workflow

1. Classify the XState surface area: machine modeling, actors, context, events, transitions, guards, actions, invoke, persistence, React integration, TypeScript, testing, or migration.
2. Fetch `https://stately.ai/llms.txt` for the concise map.
3. Fetch `https://stately.ai/llms-full.txt` only when the concise map points to a detailed section, the question needs examples, or the implementation depends on exact API behavior.
4. Extract the minimum relevant guidance for the user's exact request.
5. Provide concrete code or review guidance using XState terminology.
6. Completion: the answer or code change is grounded in Stately docs, and any assumptions or source conflicts are stated explicitly.

## Output Requirements

- Prefer practical, implementation-ready recommendations.
- Match the user's framework/language (TypeScript, React, etc.).
- When uncertain, explicitly state assumptions and what needs validation.
- Keep terminology consistent with XState docs (`machine`, `state`, `event`, `actor`, `invoke`).
