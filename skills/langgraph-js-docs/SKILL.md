---
name: langgraph-js-docs
description: LangChain and LangGraph JS/TS docs lookup for LangChain.js, LangGraph.js, and LangSmith SDK questions. Use the docs sitemap search and TypeDoc API reference before answering SDK questions or changing code.
---

# LangChain + LangGraph JS/TS Docs Search

## Canonical doc roots (prefer these)

- LangChain OSS JS/TS docs: `https://docs.langchain.com/oss/javascript/langchain/`
- LangGraph OSS JS/TS docs: `https://docs.langchain.com/oss/javascript/langgraph/`
- JS/TS integrations: `https://docs.langchain.com/oss/javascript/integrations/`
- JS/TS reference hub: `https://docs.langchain.com/oss/javascript/reference/overview`
- JS/TS API reference (TypeDoc): `https://reference.langchain.com/javascript/`
- LangSmith JS/TS SDK docs: `https://docs.langchain.com/langsmith/` (see references)
- LLM-friendly index (useful for discovery): `https://docs.langchain.com/llms.txt`

## Workflow

1. Classify the user question:

   - LangChain (runnables, prompts, tools, RAG, models, parsers)
   - LangGraph (graphs, nodes/edges, state, checkpointers, streaming, interrupts)
   - LangSmith (tracing, evals, SDK, LangGraph platform tooling)

2. Find the right docs page:

   - Prefer sitemap-driven URL search:
     - Run `scripts/langchain_docs_search.py` with a few keywords from the question.
     - Constrain to `--area oss-js` for most LangChain/LangGraph topics.
   - If you need citations or the script is unavailable, use web search recipes:
     - `site:docs.langchain.com/oss/javascript/langchain <keywords>`
     - `site:docs.langchain.com/oss/javascript/langgraph <keywords>`
     - `site:docs.langchain.com/oss/javascript/integrations <provider/tool>`

3. When you need signatures and exact symbol locations:

   - Go to `https://reference.langchain.com/javascript/` and search for the symbol name.
   - If you already know the package/module:
     - LangChain core APIs often live under `@langchain/core` and show up in modules under `langchain` (TypeDoc groups vary by version).
     - LangGraph JS APIs often live under `@langchain/langgraph` and show up under modules related to `@langchain/langgraph`.

4. Sanity-check version pitfalls before final guidance:

   - Recent docs assume Node 20+ and LangChain/LangGraph v1+.
   - Package splits are common: `@langchain/core`, `@langchain/openai`, `@langchain/langgraph`, and legacy APIs may be under `@langchain/classic`.

5. Completion: the answer or code change is grounded in a JS/TS docs page or TypeDoc symbol page, and version/package-split caveats have been checked when relevant.

## Resources in this skill

- `scripts/langchain_docs_search.py`: Download the official docs or TypeDoc sitemap, then search URLs with JS/TS-focused ranking.
- `references/doc-roots.md`: Curated roots + high-signal landing pages.
- `references/query-cheatsheet.md`: Common user phrases -> suggested doc roots and search keywords.
- `references/api-reference-notes.md`: TypeDoc entry points and how to locate modules.
