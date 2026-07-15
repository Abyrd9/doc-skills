#!/usr/bin/env python3

"""Rank Lucia documentation routes against a natural-language query."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class DocRoute:
    title: str
    url: str
    tags: tuple[str, ...]


DOC_ROUTES = (
    DocRoute(
        title="Sessions overview",
        url="https://lucia-auth.com/sessions/overview",
        tags=(
            "session",
            "cookie",
            "auth",
            "database",
            "validation",
            "renew",
            "overview",
        ),
    ),
    DocRoute(
        title="Sessions basic implementation",
        url="https://lucia-auth.com/sessions/basic",
        tags=("session", "implement", "basic", "cookie", "database", "token"),
    ),
    DocRoute(
        title="Sessions inactivity timeout",
        url="https://lucia-auth.com/sessions/inactivity-timeout",
        tags=("session", "timeout", "idle", "sliding", "expiration", "renew"),
    ),
    DocRoute(
        title="Sessions stateless tokens",
        url="https://lucia-auth.com/sessions/stateless-tokens",
        tags=("session", "stateless", "token", "jwt", "bearer"),
    ),
    DocRoute(
        title="Sessions frameworks",
        url="https://lucia-auth.com/sessions/frameworks",
        tags=("session", "framework", "nextjs", "sveltekit", "runtime"),
    ),
    DocRoute(
        title="GitHub OAuth tutorial",
        url="https://lucia-auth.com/tutorials/github-oauth",
        tags=("github", "oauth", "login", "provider", "tutorial"),
    ),
    DocRoute(
        title="Google OAuth tutorial",
        url="https://lucia-auth.com/tutorials/google-oauth",
        tags=("google", "oauth", "login", "provider", "tutorial"),
    ),
    DocRoute(
        title="GitHub OAuth example",
        url="https://lucia-auth.com/examples/github-oauth",
        tags=("github", "oauth", "example", "repo", "framework"),
    ),
    DocRoute(
        title="Google OAuth example",
        url="https://lucia-auth.com/examples/google-oauth",
        tags=("google", "oauth", "example", "repo", "framework"),
    ),
    DocRoute(
        title="Email password with 2FA example",
        url="https://lucia-auth.com/examples/email-password-2fa",
        tags=("email", "password", "2fa", "totp", "example"),
    ),
    DocRoute(
        title="Email password with 2FA and WebAuthn example",
        url="https://lucia-auth.com/examples/email-password-2fa-webauthn",
        tags=("email", "password", "2fa", "webauthn", "passkey", "example"),
    ),
    DocRoute(
        title="Token bucket rate limiting",
        url="https://lucia-auth.com/rate-limit/token-bucket",
        tags=("rate", "limit", "throttle", "token", "bucket", "bruteforce"),
    ),
    DocRoute(
        title="Lucia v3 migrate",
        url="https://lucia-auth.com/lucia-v3/migrate",
        tags=("migrate", "migration", "v3", "legacy", "upgrade"),
    ),
    DocRoute(
        title="Lucia v3 tutorials",
        url="https://v3.lucia-auth.com/tutorials/",
        tags=("v3", "legacy", "tutorial", "oauth", "session"),
    ),
    DocRoute(
        title="Lucia v3 OAuth guides",
        url="https://v3.lucia-auth.com/guides/oauth/",
        tags=("v3", "legacy", "oauth", "provider", "guide"),
    ),
    DocRoute(
        title="Lucia v3 GitHub OAuth tutorial",
        url="https://v3.lucia-auth.com/tutorials/github-oauth/",
        tags=("v3", "legacy", "github", "oauth", "tutorial"),
    ),
    DocRoute(
        title="Lucia v2 sessions basics",
        url="https://v2.lucia-auth.com/basics/sessions/",
        tags=("v2", "legacy", "session", "cookie", "basic"),
    ),
    DocRoute(
        title="Lucia v2 guidebook",
        url="https://v2.lucia-auth.com/guidebook/",
        tags=("v2", "legacy", "guidebook", "oauth", "session"),
    ),
    DocRoute(
        title="Lucia v2 GitHub OAuth guidebook",
        url="https://v2.lucia-auth.com/guidebook/github-oauth/",
        tags=("v2", "legacy", "github", "oauth", "guidebook"),
    ),
)


def tokenize(query: str) -> list[str]:
    """Split a natural-language query into lowercase keyword tokens."""
    return re.findall(r"[a-z0-9]+", query.lower())


def score_route(route: DocRoute, query_tokens: list[str]) -> int:
    """Score a route by overlap with route title, URL, and curated tags."""
    haystack = " ".join((route.title, route.url, *route.tags)).lower()
    return sum(1 for token in query_tokens if token in haystack)


def main() -> None:
    """Print the top matching Lucia docs routes for a query."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Natural-language Lucia docs query")
    parser.add_argument(
        "--limit", type=int, default=5, help="Maximum number of routes to print"
    )
    args = parser.parse_args()

    query_tokens = tokenize(args.query)
    ranked_routes = sorted(
        ((score_route(route, query_tokens), route) for route in DOC_ROUTES),
        key=lambda item: (-item[0], item[1].title),
    )

    for score, route in ranked_routes[: args.limit]:
        print(f"{score:>2}  {route.title}\n    {route.url}")


if __name__ == "__main__":
    main()
