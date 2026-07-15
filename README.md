# Andrew Byrd's Documentation Skills

Agent skills that consult current official documentation before answering questions or changing code. They are designed to reduce stale framework and API advice.

For code planning and review skills, see [Abyrd9/skills](https://github.com/Abyrd9/skills).

## Install

```sh
npx skills add Abyrd9/doc-skills
```

Install one skill with `--skill`:

```sh
npx skills add Abyrd9/doc-skills --skill react-docs
```

## Runtime and Platform Skills

- **`bun-docs`** — Looks up current Bun runtime, package manager, test runner, and API documentation.
- **`capacitor-docs`** — Covers Capacitor configuration, native projects, plugins, migrations, debugging, and releases.
- **`electron-docs`** — Covers Electron architecture, secure IPC, packaging, signing, updates, and distribution.
- **`openai-realtime-docs`** — Uses current OpenAI Realtime documentation for WebRTC, WebSockets, voice agents, events, tools, and costs.

## Library and Framework Skills

- **`drizzle-docs`** — Covers Drizzle ORM schemas, queries, migrations, dialects, relations, and transactions.
- **`langgraph-js-docs`** — Searches current LangChain.js, LangGraph.js, LangSmith SDK, and TypeDoc references.
- **`lexical-docs`** — Covers Lexical editors, React bindings, commands, nodes, transforms, selection, and serialization.
- **`lucia-docs`** — Uses official Lucia material for sessions, OAuth, rate limiting, and version migrations.
- **`react-docs`** — Looks up current React guidance for components, Hooks, state, Effects, Suspense, Server Components, and the React Compiler.
- **`react-effects-docs`** — Focuses on deciding when Effects, event handlers, derived state, and memoization are appropriate.
- **`tanstack-docs`** — Looks up current documentation across the TanStack ecosystem and its command-line tools.
- **`xstate-docs`** — Covers XState machines, actors, guards, actions, context, React integration, testing, and migrations.
