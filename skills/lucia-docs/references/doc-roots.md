# Lucia doc roots

## Current docs

- Home: `https://lucia-auth.com/`
- Sessions overview: `https://lucia-auth.com/sessions/overview`
- Sessions basic implementation: `https://lucia-auth.com/sessions/basic`
- Sessions inactivity timeout: `https://lucia-auth.com/sessions/inactivity-timeout`
- Sessions stateless tokens: `https://lucia-auth.com/sessions/stateless-tokens`
- Sessions frameworks: `https://lucia-auth.com/sessions/frameworks`
- GitHub OAuth tutorial: `https://lucia-auth.com/tutorials/github-oauth`
- Google OAuth tutorial: `https://lucia-auth.com/tutorials/google-oauth`
- GitHub OAuth example: `https://lucia-auth.com/examples/github-oauth`
- Google OAuth example: `https://lucia-auth.com/examples/google-oauth`
- Email/password + 2FA example: `https://lucia-auth.com/examples/email-password-2fa`
- Email/password + 2FA + WebAuthn example: `https://lucia-auth.com/examples/email-password-2fa-webauthn`
- Token bucket rate limiting: `https://lucia-auth.com/rate-limit/token-bucket`
- Lucia v3 migration: `https://lucia-auth.com/lucia-v3/migrate`

## Legacy docs to check when the question is versioned

- v3 tutorials index: `https://v3.lucia-auth.com/tutorials/`
- v3 OAuth guides: `https://v3.lucia-auth.com/guides/oauth/`
- v3 GitHub OAuth tutorial: `https://v3.lucia-auth.com/tutorials/github-oauth/`
- v2 sessions basics: `https://v2.lucia-auth.com/basics/sessions/`
- v2 guidebook: `https://v2.lucia-auth.com/guidebook/`
- v2 GitHub OAuth guidebook: `https://v2.lucia-auth.com/guidebook/github-oauth/`

## Query map

- Session storage, cookies, validation, renewal -> start with `sessions/overview`, then `sessions/basic`
- Idle timeout or sliding expiration -> `sessions/inactivity-timeout`
- JWT or token-only auth -> `sessions/stateless-tokens`
- Framework caveats -> `sessions/frameworks`
- GitHub or Google login flows -> `tutorials/*-oauth`, then matching `examples/*-oauth`
- 2FA or WebAuthn -> `examples/email-password-2fa*`
- Brute-force or auth throttling -> `rate-limit/token-bucket`
- Migrating old Lucia installs -> `lucia-v3/migrate`, then `v3.lucia-auth.com` or `v2.lucia-auth.com` pages when the user names an older version
