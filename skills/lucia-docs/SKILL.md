---
name: lucia-docs
description: Lucia docs lookup for `lucia-auth.com`, sessions, OAuth tutorials, rate limiting, Lucia v3 migration, and legacy Lucia v2/v3 questions. Search official docs before giving authentication implementation advice.
---

# Lucia Docs Search

Use Lucia official docs as the first source of truth for implementation questions.

## Canonical sources

- Current docs: `https://lucia-auth.com/`
- Archived Lucia v3 docs: `https://v3.lucia-auth.com/`
- Archived Lucia v2 docs: `https://v2.lucia-auth.com/`
- Curated route list: `references/doc-roots.md`
- Local route ranker: `scripts/lucia_docs_search.py`

## Workflow

1. Classify the question before searching.
2. Prefer current `lucia-auth.com` pages unless the user explicitly mentions Lucia v2 or v3, or the topic is clearly migration-focused.
3. Run `python3 scripts/lucia_docs_search.py "<query>"` from this skill directory to get the best official starting routes.
4. Fetch the top candidate page as markdown when the available web/docs tool supports it.
5. If the question needs implementation detail, fetch one adjacent route from the same section:
   - sessions -> another `sessions/*` page
   - OAuth -> matching `tutorials/*-oauth` and `examples/*-oauth`
   - migration -> `lucia-v3/migrate` plus the relevant archived v3/v2 page
6. Answer from those pages first. Use general web search only if the official docs do not cover the question.
7. Completion: the answer is grounded in current Lucia docs or the explicitly selected archived version, with any version mismatch called out.

## Route selection heuristics

- Sessions, cookies, renewal, validation -> start with `sessions/overview` or `sessions/basic`
- Idle expiration or sliding sessions -> `sessions/inactivity-timeout`
- Stateless auth or JWT-style flows -> `sessions/stateless-tokens`
- Framework-specific caveats -> `sessions/frameworks`
- GitHub or Google OAuth -> matching tutorial first, then matching example
- 2FA or WebAuthn -> `examples/email-password-2fa*`
- Rate limiting or brute-force protection -> `rate-limit/token-bucket`
- Older installs or API changes -> `lucia-v3/migrate`, then archived docs if needed

## Version handling

- Treat `lucia-auth.com` as the default for current guidance.
- When the user says `Lucia v3`, `Lucia v2`, or shows old APIs/imports, switch to the matching archived site.
- If the question mixes old and new Lucia concepts, call out the version mismatch explicitly before recommending code.

## Output rules

- Prefer official Lucia docs over blog posts or framework-generic auth advice.
- State which doc page(s) guidance came from when the answer is version-sensitive.
- Keep code examples minimal and aligned with the specific Lucia doc route you used.
- If Lucia docs intentionally present implementation notes instead of a reusable package API, frame the answer as an auth pattern, not a library wrapper.
