---
name: lexical-docs
description: Lexical docs lookup for Lexical editor, `@lexical/*`, React bindings, commands, nodes, transforms, selection, serialization, and editor-state work. Use lexical.dev sitemap-driven fetching before giving implementation guidance.
---

# Lexical Docs

Use Lexical official docs as the first source of truth for Lexical implementation work.

## Triggers

Treat these as triggers:

- User mentions `Lexical`, `lexical.dev`, `@lexical/*`, `lexical-react`, `LexicalComposer`, `EditorState`, nodes, commands, transforms, serialization.
- The task touches `editor.update(...)`, `editorState.read(...)`, selection, history, HTML import/export, or custom nodes.

## Deterministic sitemap workflow

Use this lookup sequence (no guessing routes):

1. Fetch `https://lexical.dev/sitemap.xml`.
2. Filter to sitemap URLs under `/docs/`.
3. Pick the smallest set of highly relevant routes (prefer exact concept matches over broad pages).
4. If the question is API-shaped ("what does X do?", "what params?", "what does this helper return?"), prefer `https://lexical.dev/docs/api/` and `https://lexical.dev/docs/api/modules/*` routes over narrative docs.
5. Fetch each candidate page as markdown when the available web/docs tool supports it.
6. Answer from those pages; if coverage is missing, fetch 1-2 adjacent pages from the sitemap before using non-doc sources.
7. Completion: the answer or code change is grounded in the fetched Lexical docs or explicitly says the docs did not cover the needed detail.

## API modules workflow

When the question names a symbol (function/class/command/hook/plugin), use this module-first approach:

1. Fetch `https://lexical.dev/docs/api/` and identify the relevant module.
2. Prefer the closest matching module under `https://lexical.dev/docs/api/modules/`:

- Core: `https://lexical.dev/docs/api/modules/lexical`
- React bindings: modules prefixed with `lexical_react_...`
- Package modules: `lexical_list`, `lexical_table`, `lexical_link`, `lexical_history`, `lexical_markdown`, `lexical_selection`, `lexical_utils`, etc.

3. Fetch that module page and verify the exact signature/behavior from the API listing.
4. If the symbol isn’t in that module, fetch the next-closest module from the sitemap (1-2 tries).

Secondary source (only if docs are thin): consult official examples in `facebook/lexical`:

- `examples/react-rich/src/App.tsx`
- `packages/lexical-playground/src/Editor.tsx`

## Key routes to check first

- `https://lexical.dev/docs/intro`
- `https://lexical.dev/docs/getting-started/react`
- `https://lexical.dev/docs/getting-started/quick-start`
- `https://lexical.dev/docs/concepts/editor-state`
- `https://lexical.dev/docs/concepts/updates`
- `https://lexical.dev/docs/concepts/commands`
- `https://lexical.dev/docs/concepts/nodes`
- `https://lexical.dev/docs/serialization/`
- `https://lexical.dev/docs/extensions/intro`
- `https://lexical.dev/docs/react/`
- `https://lexical.dev/docs/packages/lexical-react`
- `https://lexical.dev/docs/api/` (then modules, especially `https://lexical.dev/docs/api/modules/lexical`)

If you need exhaustive API surface area, enumerate modules from the sitemap under:

- `https://lexical.dev/docs/api/modules/`

## Common pitfalls (use as a checklist)

- Keep reads/writes inside `editorState.read(...)` and `editor.update(...)`; avoid mutating outside transactions.
- Async work: don’t hold Lexical node references across awaits; re-read inside a fresh transaction.
- History + discrete updates: be explicit about update modes when user expects undo/redo behavior.
- Node transforms: avoid transform loops and be careful with focus/selection side effects.
- Selection: watch for selection loss when replacing nodes; decorator node selection is easy to break.
- HTML export in headless environments may need a DOM polyfill.
- Deserialization: ensure custom nodes are registered before parsing JSON; unregistered nodes can drop content.

## Version-sensitive APIs

When imports, serialization, or transform behavior appear version-sensitive, verify the current API module page before recommending code and call out the version boundary only if the official docs or release notes establish it.

## Output rules

- Prefer Lexical docs over general DOM/contenteditable advice; use secondary sources only when docs don’t cover it.
- When suggesting APIs that moved/changed, call out the version-sensitive import/behavior explicitly.
- Keep answers implementation-focused: show the minimal code pattern and where it belongs (update/read, plugin, node, command).
