---
name: react-docs
description: React docs workflow for components, JSX/TSX, Hooks, state, Effects, forms, lists, context, refs, Suspense, Server Components, React DOM, performance, and React Compiler behavior. Use current official React docs before React-specific design or code changes.
---

# React Docs

Use official React docs as the default source of truth before making React code changes.

## Canonical Sources

- Docs index for agents: `https://react.dev/llms.txt`
- Learn landing page: `https://react.dev/learn.md`
- Component design: `https://react.dev/learn/thinking-in-react.md`
- State structure: `https://react.dev/learn/choosing-the-state-structure.md`
- Effects decision guide: `https://react.dev/learn/you-might-not-need-an-effect.md`
- Effect synchronization: `https://react.dev/learn/synchronizing-with-effects.md`
- Effect dependencies: `https://react.dev/learn/removing-effect-dependencies.md`
- React Compiler: `https://react.dev/learn/react-compiler.md`
- React API reference: `https://react.dev/reference/react.md`
- React DOM reference: `https://react.dev/reference/react-dom.md`
- Rules of React: `https://react.dev/reference/rules.md`

## Workflow

1. Detect the React surface area before editing: components, Hooks, Effects, forms, lists, context, reducers, refs, Suspense, Server Components, React DOM, or compiler behavior.
2. Fetch `https://react.dev/llms.txt` and choose the smallest set of official pages relevant to the task.
3. Read the relevant official pages before proposing or applying React-specific changes.
4. Inspect the local codebase for its React version, framework conventions, compiler setup, lint rules, and existing component patterns.
5. Prefer the simplest React-native design that follows the docs and the local codebase style.
6. Make the smallest correct change, then run the repo's normal lint/test/build checks.
7. In the final response, mention the React docs pages that influenced the decision when the change is non-trivial.
8. Completion: relevant React docs were consulted, local conventions were checked, and verification was run or explicitly skipped with a reason.

## Page Selection

- New or redesigned UI: read `Thinking in React`, `Passing Props to a Component`, `Rendering Lists`, and `Conditional Rendering` as needed.
- State modeling: read `Choosing the State Structure`, `Sharing State Between Components`, and `Preserving and Resetting State`.
- Effects or dependencies: read `You Might Not Need an Effect`, `Synchronizing with Effects`, and `Removing Effect Dependencies`.
- Custom Hooks: read `Reusing Logic with Custom Hooks` and the specific Hook API reference.
- Forms and DOM elements: read the relevant `react-dom/components/*` reference page.
- Performance or memoization: read `React Compiler`, `useMemo`, `useCallback`, `memo`, `useDeferredValue`, `useTransition`, or `startTransition` as appropriate.
- Server/client boundaries: read the React Server Components docs and directive pages such as `use client` and `use server`.
- Hook or purity errors: read `Rules of Hooks`, `Components and Hooks must be pure`, and the relevant eslint-plugin-react-hooks lint page.

## Decision Rules

- Components and Hooks must be pure; keep rendering deterministic and side-effect free.
- Model state as the minimal complete representation. Derive everything else during render when possible.
- Prefer one-way data flow: pass data down, pass event handlers up, and lift state only when multiple components need the same source of truth.
- Use Effects only to synchronize with external systems. Do not use Effects for render-time derivations or event-specific logic.
- Prefer event handlers for logic caused by a user interaction.
- Prefer keys, controlled components, or derived values over Effects for resetting or mirroring state.
- Do not add `useMemo`, `useCallback`, or `memo` by default. Use them when the docs and measurements or codebase constraints justify it, especially considering React Compiler.
- Keep refs as escape hatches for values or DOM interactions, not as a substitute for render state.
- Follow official Hook rules and preserve dependency correctness instead of suppressing lint rules.

## Output Rules

When using this skill, include:

- which React docs pages were consulted or should be consulted
- the React principle that drove the implementation or review finding
- any local project convention that overrode a generic React recommendation
- verification performed, or why verification was not run
