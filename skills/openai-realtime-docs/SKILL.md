---
name: openai-realtime-docs
description: OpenAI Realtime docs workflow for Realtime API, WebRTC, WebSocket, voice agents, live transcription/translation, session config, ephemeral client secrets, client/server events, VAD, tools/MCP, server controls, prompting, and cost work.
---

# OpenAI Realtime Docs

## Source Priority

Use current official OpenAI documentation before giving advice or changing code.

1. Prefer the OpenAI developer docs MCP tools when they are exposed in the current tool surface:
   - `mcp__openaiDeveloperDocs__search_openai_docs`
   - `mcp__openaiDeveloperDocs__fetch_openai_doc`
   - `mcp__openaiDeveloperDocs__list_openai_docs`
2. If those tools are not available, use only official OpenAI domains:
   - `https://developers.openai.com/api/docs/...`
   - `https://platform.openai.com/docs/...`
3. Do not rely on mirrored docs, third-party tutorials, or stale beta snippets when official pages differ.
4. For implementation work, fetch the exact page for the relevant transport, event, or API reference before coding.

## Core Workflow

1. Classify the task:
   - Browser/mobile realtime voice -> WebRTC.
   - Backend-to-OpenAI realtime audio/event bridge -> WebSocket.
   - Higher-level agent orchestration -> Voice Agents / Agents SDK docs.
   - Speech-to-text only -> Realtime transcription docs.
   - Language conversion -> Realtime translation docs.
   - Tool calls, MCP, or guardrails -> Realtime tools and server controls docs.
   - Latency, turn taking, interruptions -> VAD and conversation docs.
   - Spend optimization -> Realtime costs docs.
2. Read [references/realtime-doc-map.md](references/realtime-doc-map.md), then open the linked official docs for the selected lane.
3. Identify the current API generation and endpoint shape from docs. Be careful with old beta examples and headers.
4. Design session flow before coding:
   - Server creates short-lived client secret / ephemeral token when clients connect directly.
   - Client establishes WebRTC or WebSocket session using that secret.
   - Client/server sends session configuration and events.
   - App handles server events, conversation state, interruptions, tool calls, and teardown.
5. Keep credentials server-side. Never put a standard OpenAI API key in browser or mobile client code.
6. Validate behavior with the relevant event reference, not just guide snippets.
7. Completion: the implementation or answer is grounded in current official OpenAI docs for the chosen transport and event/session surface.

## Transport Guidance

Prefer WebRTC for browser and mobile audio because it handles realtime media transport, microphone input, playback, and network conditions better for direct client experiences.

Prefer WebSocket when the app is a backend service, telephony bridge, server-side audio pipeline, custom media stack, or needs explicit event stream handling outside the browser.

Use the Voice Agents docs when the user wants higher-level agent concepts such as handoffs, guardrails, tools, session history, or SDK-managed transport rather than raw Realtime events.

## Implementation Guardrails

- Treat session configuration as an explicit contract: model, voice, modalities, audio formats, instructions, tools, turn detection, transcription, and token limits should be set deliberately.
- Use ephemeral client secrets for untrusted clients; standard API keys stay on trusted servers only.
- Read both client event and server event references before building event reducers.
- Model tool calls as asynchronous lifecycle events; do not assume one response event contains the whole interaction.
- Account for interruptions and cancellation when audio output is in progress.
- Decide whether server VAD, semantic VAD, or manual turn control fits the product before tuning thresholds.
- For transcription-only use cases, use transcription-specific session docs and do not overbuild a bidirectional voice agent.
- For costs, inspect audio token usage, prompt caching, session lifetime, idle timeouts, and truncation behavior in the current docs.

## Common Deliverables

When asked to help build or review a Realtime integration, produce:

- Chosen transport and why.
- Session creation flow and credential boundary.
- Event flow diagram or ordered list.
- Minimal session configuration.
- Client event handlers and server event handlers to implement.
- Tool/VAD/conversation/cost considerations that apply.
- Official docs consulted, with links.
