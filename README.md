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
- **`expo-docs`** — Uses SDK-matched Expo documentation after routing implementation tasks through [Expo's official plugin](https://github.com/expo/skills).
- **`react-native-docs`** — Uses version-matched React Native documentation for core APIs, styles, accessibility, testing, and upgrades.

## Library and Framework Skills

- **`drizzle-docs`** — Covers Drizzle ORM schemas, queries, migrations, dialects, relations, and transactions.
- **`effect-docs`** — Uses installed Effect package guidance and current official docs for exact APIs and versions.
- **`langgraph-js-docs`** — Searches current LangChain.js, LangGraph.js, LangSmith SDK, and TypeDoc references.
- **`lexical-docs`** — Covers Lexical editors, React bindings, commands, nodes, transforms, selection, and serialization.
- **`lucia-docs`** — Uses Lucia's current session guide and Auth Book, with official archives for old Lucia versions.
- **`react-docs`** — Looks up current React guidance for components, Hooks, state, Effects, Suspense, Server Components, and the React Compiler.
- **`tanstack-docs`** — Looks up current documentation across the TanStack ecosystem and its command-line tools.

## First-party replacements

- OpenAI Realtime work is covered by Codex's bundled `openai-docs` skill.
- Effect setup and v3-to-v4 migrations use [Effect's official skills](https://github.com/Effect-TS/skills); general API work remains in `effect-docs`.
- XState work should use [Stately's official `xstate-v5` skill](https://github.com/statelyai/skills/tree/main/skills/xstate-v5).
