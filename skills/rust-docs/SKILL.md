---
name: rust-docs
description: Official Rust docs workflow for language, standard library, Cargo, compiler errors, editions, unsafe code, and crate APIs. Use before Rust-specific design, implementation, debugging, or review; match documentation to the project's toolchain, features, target, and dependency versions.
---

# Rust Docs

Use official Rust references and crate-maintainer docs before making Rust-specific decisions.

## Sources

| Need | Source |
| --- | --- |
| Documentation index | https://doc.rust-lang.org/ |
| Ownership, borrowing, lifetimes, traits, and language basics | https://doc.rust-lang.org/book/ |
| Short runnable examples | https://doc.rust-lang.org/rust-by-example/ |
| Language rules | https://doc.rust-lang.org/reference/ |
| Standard library APIs | https://doc.rust-lang.org/std/ |
| `core` and `alloc` APIs | https://doc.rust-lang.org/core/ and https://doc.rust-lang.org/alloc/ |
| Cargo manifests, workspaces, features, builds, and dependencies | https://doc.rust-lang.org/cargo/ |
| Edition changes | https://doc.rust-lang.org/edition-guide/ |
| Compiler options and targets | https://doc.rust-lang.org/rustc/ |
| Compiler error explanations | https://doc.rust-lang.org/error_codes/ |
| Documentation and doctests | https://doc.rust-lang.org/rustdoc/ |
| Clippy lints | https://doc.rust-lang.org/clippy/ |
| Unsafe Rust | https://doc.rust-lang.org/nomicon/ plus the relevant Reference and API safety sections |
| Nightly features | https://doc.rust-lang.org/unstable-book/ |
| Toolchain selection | https://rust-lang.github.io/rustup/ |
| Published crate APIs | https://docs.rs/ with an exact crate version |

## Workflow

1. Inspect `rust-toolchain.toml` or `rust-toolchain`, `Cargo.toml`, `Cargo.lock`, and `.cargo/config.toml` as relevant. Check workspace inheritance, edition, `rust-version` (minimum supported Rust version), enabled features, target, and resolved dependency versions. The edition and compiler version are separate settings.
2. Check the active compiler with `rustc --version` and, when rustup manages it, `rustup show active-toolchain`. Use the project's chosen toolchain; a moving stable or nightly channel is not a fixed version.
3. Select the smallest relevant official chapter or API page. Use the Book for explanation and the Reference or API docs for precise rules. For a compiler error, read the full diagnostic and use `rustc --explain E####` or its matching error-code page.
4. Match API availability to the supported compiler. Check standard-library stability notes and use `https://doc.rust-lang.org/<version>/` or installed toolchain docs when current docs differ. Do not treat nightly examples or unstable APIs as stable.
5. For a crate, use its exact resolved version on docs.rs and follow links to maintainer guides or source. Check feature gates and platform conditions; the docs.rs build may enable different features or targets. For Git dependencies, use source and docs at the locked revision.
6. Make the smallest change that fits the project. Run its required checks with the relevant package, target, and features. Include doctests when changing documented examples. Report the checks run and any limits.
7. Cite the pages that drove non-trivial decisions. If docs are unavailable or disagree with the installed source, state the gap and verify with source or a focused compile check.

## Local documentation

- Use `rustup doc --path` to locate installed toolchain docs without opening a browser. If absent, continue with versioned web docs.
- Use `cargo doc --locked -p <package>` when local package or dependency docs would resolve an API question. Supply the app's relevant feature and target flags; do not enable every feature by default.
- Generated docs normally live under `target/doc`; target or output-directory settings can change the path. Use `--document-private-items` when internal APIs matter.
- Documentation builds may compile dependencies and run build scripts. Use them in the project's normal build environment and keep dependency changes out of a docs lookup.

## Decisions to verify

- Check ownership and lifetime requirements before adding clones, shared ownership, locks, or `'static` bounds to satisfy an error.
- Async runtime behavior belongs to the runtime crate's docs as well as Rust's language docs.
- Read each unsafe operation's safety contract and check the code's invariants; a successful build does not prove soundness. The Reference is not a complete formal specification.
- Do not upgrade the toolchain, change editions, or enable nightly just to match a newer example unless the task calls for that change.

Keep this skill focused on finding and checking documentation, not prescribing an application architecture.
