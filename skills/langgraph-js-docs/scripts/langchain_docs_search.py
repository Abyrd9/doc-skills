#!/usr/bin/env python3
"""Sitemap-driven docs URL search for LangChain/LangGraph JS/TS.

Why this exists:
- docs.langchain.com URLs move over time. The sitemap is the most reliable current index.
- Agents frequently need to map user phrasing -> the best doc page or API reference hub.

This script:
1) Fetches https://docs.langchain.com/sitemap.xml (recurses if it's a sitemap index)
2) Extracts URLs
3) Ranks results for JS/TS docs, then prints top matches

Examples:
  python3 scripts/langchain_docs_search.py "tool calling" --area oss-js
  python3 scripts/langchain_docs_search.py "StateGraph addConditionalEdges" --area oss-js
  python3 scripts/langchain_docs_search.py "LangSmith JS SDK tracing" --area langsmith-js
  python3 scripts/langchain_docs_search.py "RunnableSequence" --area all --top 25
"""

from __future__ import annotations

import argparse
import gzip
import json
import os
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import Iterable, Optional


SITEMAP_URL_DEFAULT = "https://docs.langchain.com/sitemap.xml"
REFERENCE_SITEMAP_URL = "https://reference.langchain.com/sitemap.xml"
CACHE_TTL_SECONDS = 24 * 60 * 60


@dataclass(frozen=True)
class UrlEntry:
    loc: str
    lastmod: Optional[str] = None


def _read_url_bytes(url: str, timeout_s: int) -> bytes:
    """Fetch a URL as bytes; transparently handle gzip encoding."""
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "opencode-skill/langchain-langgraph-js-docs (sitemap fetch)"
        },
    )
    with urllib.request.urlopen(req, timeout=timeout_s) as resp:
        data = resp.read()
        enc = (resp.headers.get("Content-Encoding") or "").lower()
        if enc == "gzip":
            return gzip.decompress(data)
        return data


def _xml_root_tag(local_name: str) -> str:
    return "{http://www.sitemaps.org/schemas/sitemap/0.9}" + local_name


def _parse_sitemap_xml(xml_bytes: bytes) -> tuple[str, ET.Element]:
    """Return (kind, root) where kind is 'urlset' or 'sitemapindex'."""
    root = ET.fromstring(xml_bytes)
    tag = root.tag
    if tag.endswith("urlset"):
        return ("urlset", root)
    if tag.endswith("sitemapindex"):
        return ("sitemapindex", root)
    # Some publishers omit/alter namespaces; fall back to suffix checks.
    if tag == "urlset":
        return ("urlset", root)
    if tag == "sitemapindex":
        return ("sitemapindex", root)
    raise ValueError(f"Unsupported sitemap root tag: {tag}")


def _extract_urlset_entries(root: ET.Element) -> list[UrlEntry]:
    entries: list[UrlEntry] = []
    for url_el in root.findall(_xml_root_tag("url")) or root.findall("url"):
        loc_el = url_el.find(_xml_root_tag("loc"))
        if loc_el is None:
            loc_el = url_el.find("loc")
        if loc_el is None or not (loc_el.text or "").strip():
            continue
        lastmod_el = url_el.find(_xml_root_tag("lastmod"))
        if lastmod_el is None:
            lastmod_el = url_el.find("lastmod")
        entries.append(
            UrlEntry(
                loc=(loc_el.text or "").strip(),
                lastmod=((lastmod_el.text or "").strip() if lastmod_el is not None else None),
            )
        )
    return entries


def _extract_sitemapindex_locs(root: ET.Element) -> list[str]:
    locs: list[str] = []
    for sm_el in root.findall(_xml_root_tag("sitemap")) or root.findall("sitemap"):
        loc_el = sm_el.find(_xml_root_tag("loc"))
        if loc_el is None:
            loc_el = sm_el.find("loc")
        if loc_el is None:
            continue
        loc = (loc_el.text or "").strip()
        if loc:
            locs.append(loc)
    return locs


def _walk_sitemaps(
    start_url: str,
    *,
    timeout_s: int,
    max_sitemaps: int,
) -> list[UrlEntry]:
    """Fetch start_url; if it's an index, recurse to child sitemaps."""
    seen: set[str] = set()
    queue: list[str] = [start_url]
    all_entries: list[UrlEntry] = []

    while queue:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        if len(seen) > max_sitemaps:
            raise RuntimeError(f"Exceeded max_sitemaps={max_sitemaps}")

        xml_bytes = _read_url_bytes(url, timeout_s=timeout_s)
        kind, root = _parse_sitemap_xml(xml_bytes)

        if kind == "urlset":
            all_entries.extend(_extract_urlset_entries(root))
            continue

        child_locs = _extract_sitemapindex_locs(root)
        queue.extend(child_locs)

    return all_entries


def _normalize_tokens(query: str) -> list[str]:
    """Tokenize query for URL matching (very lightweight; URLs are short)."""
    query = query.strip().lower()
    # Split on whitespace and common punctuation.
    raw = re.split(r"[^a-z0-9_@/.-]+", query)
    tokens = [t for t in raw if t and len(t) >= 2]
    # De-dupe while preserving order.
    seen: set[str] = set()
    out: list[str] = []
    for t in tokens:
        if t in seen:
            continue
        seen.add(t)
        out.append(t)
    return out


def _area_prefixes(area: str) -> list[str]:
    if area == "oss-js":
        return ["https://docs.langchain.com/oss/javascript/"]
    if area == "reference-js":
        return ["https://reference.langchain.com/javascript/"]
    if area == "langsmith-js":
        return ["https://docs.langchain.com/langsmith/"]
    if area == "all":
        return [
            "https://docs.langchain.com/oss/javascript/",
            "https://docs.langchain.com/langsmith/",
            "https://reference.langchain.com/javascript/",
        ]
    raise ValueError(f"Unknown area: {area}")


def _score_url(loc: str, tokens: list[str]) -> float:
    """Score a URL; higher is better. Optimized for JS/TS docs discovery."""
    u = loc.lower()
    score = 0.0

    # Strong boosts for the JS/TS doc roots.
    if u.startswith("https://docs.langchain.com/oss/javascript/"):
        score += 50.0
    if u.startswith("https://reference.langchain.com/javascript/"):
        score += 40.0
    if u.startswith("https://docs.langchain.com/langsmith/"):
        score += 20.0

    # Penalize other ecosystems.
    if "/oss/python/" in u:
        score -= 100.0

    # Token matches.
    for t in tokens:
        if t in u:
            score += 10.0

    # Prefer landing pages / overview pages when token match is weak.
    if u.endswith("/overview") or u.endswith("/overview/"):
        score += 2.0
    if u.endswith("/install") or u.endswith("/install/"):
        score += 1.0
    if u.endswith("/quickstart") or u.endswith("/quickstart/"):
        score += 1.0

    return score


def _filter_by_prefix(urls: Iterable[UrlEntry], prefixes: list[str]) -> list[UrlEntry]:
    out: list[UrlEntry] = []
    for e in urls:
        for p in prefixes:
            if e.loc.startswith(p):
                out.append(e)
                break
    return out


def _filter_by_regex(urls: Iterable[UrlEntry], include: Optional[str], exclude: Optional[str]) -> list[UrlEntry]:
    inc_re = re.compile(include, re.IGNORECASE) if include else None
    exc_re = re.compile(exclude, re.IGNORECASE) if exclude else None
    out: list[UrlEntry] = []
    for e in urls:
        if inc_re and not inc_re.search(e.loc):
            continue
        if exc_re and exc_re.search(e.loc):
            continue
        out.append(e)
    return out


def _cache_path_default(area: str) -> str:
    base = os.path.join(os.path.expanduser("~"), ".cache", "langchain-js-docs")
    return os.path.join(base, f"{area}-sitemap-urls.json")


def _load_cache(cache_path: str, sources: list[str]) -> Optional[list[UrlEntry]]:
    try:
        with open(cache_path, "r", encoding="utf-8") as f:
            payload = json.load(f)
        generated_at = payload.get("generatedAt")
        if not isinstance(generated_at, int) or time.time() - generated_at > CACHE_TTL_SECONDS:
            return None
        if payload.get("sources") != sources:
            return None
        urls = payload.get("urls")
        if not isinstance(urls, list):
            return None
        out: list[UrlEntry] = []
        for item in urls:
            if isinstance(item, str):
                out.append(UrlEntry(loc=item))
            elif isinstance(item, dict) and isinstance(item.get("loc"), str):
                out.append(UrlEntry(loc=item["loc"], lastmod=item.get("lastmod")))
        return out
    except FileNotFoundError:
        return None
    except Exception:
        return None


def _write_cache(cache_path: str, sources: list[str], entries: list[UrlEntry]) -> None:
    cache_dir = os.path.dirname(cache_path)
    if cache_dir:
        os.makedirs(cache_dir, exist_ok=True)
    payload = {
        "generatedAt": int(time.time()),
        "sources": sources,
        "urls": [{"loc": e.loc, "lastmod": e.lastmod} for e in entries],
    }
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, sort_keys=True)
        f.write("\n")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("query", help="search terms (matched against URL strings)")
    ap.add_argument("--sitemap", help="override the official sitemap selected by --area")
    ap.add_argument(
        "--area",
        default="oss-js",
        choices=["oss-js", "reference-js", "langsmith-js", "all"],
        help="URL subset to search",
    )
    ap.add_argument("--top", type=int, default=15, help="number of results")
    ap.add_argument("--timeout", type=int, default=25, help="fetch timeout seconds")
    ap.add_argument("--max-sitemaps", type=int, default=50, help="safety limit for index recursion")
    ap.add_argument("--include", default=None, help="regex that must match URL")
    ap.add_argument("--exclude", default=None, help="regex that must not match URL")
    ap.add_argument(
        "--cache",
        help="cache file path (JSON). Defaults to a per-area cache; set to '-' to disable caching.",
    )
    ap.add_argument(
        "--refresh",
        action="store_true",
        help="ignore cache and refetch sitemap",
    )
    args = ap.parse_args(argv)

    tokens = _normalize_tokens(args.query)
    if not tokens:
        print("No usable tokens in query.", file=sys.stderr)
        return 2

    if args.sitemap:
        sitemaps = [args.sitemap]
    elif args.area == "reference-js":
        sitemaps = [REFERENCE_SITEMAP_URL]
    elif args.area == "all":
        sitemaps = [SITEMAP_URL_DEFAULT, REFERENCE_SITEMAP_URL]
    else:
        sitemaps = [SITEMAP_URL_DEFAULT]

    cache_path = args.cache if args.cache is not None else _cache_path_default(args.area)
    entries: Optional[list[UrlEntry]] = None
    if cache_path != "-" and not args.refresh:
        entries = _load_cache(cache_path, sitemaps)

    if entries is None:
        entries = []
        for sitemap in sitemaps:
            entries.extend(_walk_sitemaps(sitemap, timeout_s=args.timeout, max_sitemaps=args.max_sitemaps))
        if cache_path != "-":
            _write_cache(cache_path, sources=sitemaps, entries=entries)

    prefixes = _area_prefixes(args.area)
    entries = _filter_by_prefix(entries, prefixes=prefixes)
    entries = _filter_by_regex(entries, include=args.include, exclude=args.exclude)

    scored = [(e, _score_url(e.loc, tokens=tokens)) for e in entries]
    scored.sort(key=lambda x: x[1], reverse=True)

    shown = 0
    for e, s in scored:
        if s <= 0:
            continue
        print(f"{s:6.1f}  {e.loc}")
        shown += 1
        if shown >= args.top:
            break

    if shown == 0:
        print("No matches.", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
