---
name: rune-docs
description: Official docs workflow for Anomaly's Rune Rust UI framework (anomalyco/rune). Use when building, changing, debugging, or reviewing Rune apps, rune-kit components and diffs, layout, motion, headless tests, or its web target. Does not cover unrelated projects named Rune.
---

# Rune Docs

Use Anomaly's official Rune docs before making Rune-specific design or code changes.

## Sources

All repository links below use `dev` for discovery. For an existing app, read the same paths at its pinned Git revision.

- Overview and setup: https://github.com/anomalyco/rune/blob/dev/README.md
- Core API and agent tooling: https://github.com/anomalyco/rune/blob/dev/crates/rune/README.md
- Components, themes, Markdown, and diffs: https://github.com/anomalyco/rune/blob/dev/crates/rune-kit/README.md
- Web target: https://github.com/anomalyco/rune/blob/dev/WEB.md
- Starting example: https://github.com/anomalyco/rune/tree/dev/examples/hello
- Other examples: https://github.com/anomalyco/rune/tree/dev/examples
- Changes: https://github.com/anomalyco/rune/blob/dev/CHANGELOG.md
- Performance guide source: https://github.com/anomalyco/rune/blob/dev/site/src/FastApps.tsx
- Performance audit helper: https://github.com/anomalyco/rune/blob/dev/scripts/app-audit

For plain text, replace `https://github.com/anomalyco/rune/blob/<rev>/` with `https://raw.githubusercontent.com/anomalyco/rune/<rev>/`.

## Workflow

1. Inspect `Cargo.toml`, `Cargo.lock`, the Rust toolchain, target platform, and existing app structure. Identify the Rune Git revision actually resolved in the lockfile.
2. Read the relevant docs and examples at that revision. Search the large core README for the needed topic instead of loading it all. Resolve relative links from their source file.
3. Use `dev` docs and the changelog to investigate newer behavior, then compare with the pinned source before using an API. Rune is pre-release; pin a concrete revision for new dependencies. Keep crates from the Rune repository on a compatible revision.
4. Start with the smallest matching example. Check source signatures when prose or examples disagree; describe any unresolved mismatch. Treat plans as intent, not proof of shipped behavior.
5. Make the smallest change that fits the app. Run its normal Rust checks. For UI changes, use Rune's headless screenshots, element tree, and scripted input as relevant; inspect the output. Check a real window or browser when behavior depends on that environment.
6. For performance work, read the matching revision's Fast apps guide. Run `scripts/app-audit <repo>` from that revision when its heuristics fit the task, then inspect each result; a hit is a place to check, not proof of a defect.
7. Cite the docs that drove non-trivial decisions and state what ran. Separate measured results from upstream performance claims.

## Choose a reference

| Task | Read |
| --- | --- |
| App setup or state/events | Overview, core README, `examples/hello` |
| Layout, scrolling, animation, text, windows | Matching core README section and linked source/example |
| Controls, overlays, themes, Markdown | rune-kit README |
| Code review, annotations, line selection | rune-kit README's Diff section and diff example |
| Screenshots or scripted UI checks | Core README's Agent tooling section |
| Browser builds or embedding | `WEB.md`, then the matching web example |
| Responsiveness, large lists, polling, or first-frame work | Fast apps guide and `scripts/app-audit` |

## Details to check

- Bound scroll viewport height and check minimum heights on nested columns. Read the growth-stack requirements before adding virtualization.
- Distinguish a patch's available context from full old/new file contents when expanding a diff.
- The web target is experimental. Check its current build, WebGPU, input, and accessibility behavior for the intended browser.
- Headless checks prove only the behavior exercised; they do not establish platform support or real display performance.

Fetch current, revision-matched guidance rather than treating this skill as a fixed API manual.
