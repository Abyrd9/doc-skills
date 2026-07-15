---
name: react-effects-docs
description: React Effects docs workflow for auditing `useEffect`, render derivations, event-handler logic, dependency reduction, `useCallback`, mirrored state, and React Compiler-related memoization choices.
---

# React Effects

Use official React docs to remove unnecessary Effects before reaching for memoization.

## Canonical sources

- Effect guidance: `https://react.dev/learn/you-might-not-need-an-effect`
- Function memoization guidance: `https://react.dev/reference/react/useCallback`
- Supporting docs when needed: `https://react.dev/learn/synchronizing-with-effects`, `https://react.dev/learn/removing-effect-dependencies`, `https://react.dev/learn/react-compiler`
- Local references: `references/effect-decision-guide.md`, `references/use-callback-guide.md`

## Workflow

1. Identify each `useEffect`, `useCallback`, and state variable involved in the problem area.
2. For every Effect, ask what external system it synchronizes with.
3. If there is no external system, replace the Effect with one of these in order of preference:
   - derive values during render
   - move logic into the event handler that caused it
   - reset with a keyed subtree
   - lift state or make the child controlled
   - use `useSyncExternalStore` for store subscriptions
4. If the Effect is real, shrink it to the smallest synchronization boundary and remove unnecessary object or function dependencies.
5. Treat `useCallback` as a performance tool, not a correctness tool. Keep it only when it protects a measured optimization or stabilizes a Hook dependency you cannot remove more directly.
6. When the codebase uses React Compiler or plans to, bias toward simpler code and fewer manual memoization hooks.
7. Completion: each touched Effect has a named external system or a replacement pattern, and each touched `useCallback` has a keep/move/delete decision.

## Decision rules

- Do not keep an Effect that only derives render data from props or state.
- Do not keep an Effect that only reacts to a user action that is already known inside an event handler.
- Prefer computing selected/filtered/transformed values during render.
- Prefer updater functions when a memoized callback only depends on previous state.
- Prefer moving helper functions inside an Effect over wrapping them in `useCallback` just to satisfy dependencies.
- Prefer a `key` reset when a prop change should reset an entire subtree.
- Prefer controlled components or lifted state when parent and child are trying to mirror each other.

Read `references/effect-decision-guide.md` when you need concrete refactor patterns and anti-pattern checks.

## useCallback guidance

- Keep `useCallback` when a stable function identity is needed for a component wrapped in `memo` or for another Hook dependency.
- Remove `useCallback` when it adds noise without a measurable rendering benefit.
- Remember that `useCallback` does not stop function creation; it only lets React reuse a cached function when dependencies are unchanged.
- If a function dependency is only used inside an Effect, first try moving the function inside the Effect.

Read `references/use-callback-guide.md` when you need examples for keeping, removing, or rewriting `useCallback`.

## Output rules

When using this skill for a review or refactor, return:

- which Effects are necessary vs unnecessary
- the recommended replacement pattern for each unnecessary Effect
- whether each `useCallback` should stay, move, or be deleted
- any dependency-array fixes and why
- whether React Compiler changes the recommendation
