# API reference notes (JS/TS)

The canonical API reference for the current JS/TS SDK is TypeDoc:

- `https://reference.langchain.com/javascript/`

Common module entry points (useful when you already know the product):

- LangChain: `https://reference.langchain.com/javascript/modules/langchain.html`
- LangGraph: `https://reference.langchain.com/javascript/modules/_langchain_langgraph.html`
- DeepAgents: `https://reference.langchain.com/javascript/modules/deepagents.html`

Tips:

- Prefer searching by exported symbol name (class/function/type), then confirm the import path.
- Many imports are package-split (common in v1+):
  - `@langchain/core` for core abstractions (runnables, messages, prompts, tools)
  - `@langchain/openai` for OpenAI models
  - `@langchain/langgraph` for LangGraph primitives
  - `@langchain/classic` for legacy APIs called out in migration guides

If a symbol is missing:

- Check if it's a legacy API that moved to `@langchain/classic`.
- Check the docs migration pages under `https://docs.langchain.com/oss/javascript/migrate/`.
