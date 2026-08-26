---
name: lucia-docs
description: Lucia docs lookup for the deprecated Lucia package, its current single-file session replacement, and archived Lucia v2/v3 guidance. Use when Lucia, lucia-auth.com, Lucia sessions, or a Lucia migration is mentioned; state the deprecation before giving current implementation advice.
---

# Lucia Docs Search

Lucia was deprecated in March 2025. The current site now points to a maintained single-file session implementation instead of the old package docs. Do not present Lucia v3 as a current package choice.

## Canonical sources

- Current status: `https://lucia-auth.com/`
- Current session implementation: `https://github.com/lucia-auth/lucia/blob/main/code/auth_session.ts`
- Maintainer's Auth Book: `https://auth.pilcrowonpaper.com/`
- Archived Lucia v3 docs: `https://v3.lucia-auth.com/`
- Archived Lucia v2 docs: `https://v2.lucia-auth.com/`
- Curated route list: `references/doc-roots.md`
- Local route ranker: `scripts/lucia_docs_search.py`

## Workflow

1. Classify the question before searching.
2. For new or current session work, start with the current status page and `code/auth_session.ts`. For broader auth design, use the Auth Book linked by the Lucia maintainer.
3. Run `python3 scripts/lucia_docs_search.py "<query>"` from this skill directory to get the best official starting routes.
4. Fetch the top candidate page as markdown when the available web/docs tool supports it.
5. If the question is about the old package, switch to the matching archived v3 or v2 site and say that the guidance is legacy.
6. Answer from those sources first. Use general web search only if the official and maintainer sources do not cover the question.
7. Completion: the answer states Lucia's deprecation and is grounded in the current replacement or the explicitly selected archived version.

## Route selection heuristics

- Current sessions, cookies, validation, and renewal -> `code/auth_session.ts`
- General auth, OAuth, 2FA, WebAuthn, and rate limiting -> the Auth Book
- Lucia v3 or v2 APIs -> the matching archived docs

## Version handling

- Treat the current `lucia-auth.com` page as a deprecation notice, not an API index.
- When the user says `Lucia v3`, `Lucia v2`, or shows old APIs/imports, switch to the matching archived site.
- If the question mixes old and new Lucia concepts, call out the version mismatch explicitly before recommending code.

## Output rules

- Prefer the current Lucia repository, archived Lucia docs, and the maintainer's Auth Book over third-party tutorials.
- State which doc page(s) guidance came from when the answer is version-sensitive.
- Keep code examples minimal and aligned with the specific Lucia doc route you used.
- If Lucia docs intentionally present implementation notes instead of a reusable package API, frame the answer as an auth pattern, not a library wrapper.
