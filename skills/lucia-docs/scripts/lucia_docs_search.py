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
        title="Current Lucia status",
        url="https://lucia-auth.com/",
        tags=(
            "current",
            "deprecated",
            "deprecation",
            "status",
            "replacement",
        ),
    ),
    DocRoute(
        title="Current session implementation",
        url="https://github.com/lucia-auth/lucia/blob/main/code/auth_session.ts",
        tags=(
            "session",
            "cookie",
            "database",
            "validation",
            "renew",
            "timeout",
            "token",
            "implementation",
        ),
    ),
    DocRoute(
        title="Auth Book",
        url="https://auth.pilcrowonpaper.com/",
        tags=(
            "auth",
            "oauth",
            "2fa",
            "webauthn",
            "passkey",
            "password",
            "rate",
            "limit",
            "security",
        ),
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
