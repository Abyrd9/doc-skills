# OpenAI Realtime Official Documentation Map

Open the relevant official page live before implementation. Realtime docs evolve quickly, especially endpoint names, GA vs beta behavior, event names, headers, model names, and session fields.

## Overview And Choosing The Right Guide

- https://developers.openai.com/api/docs/guides/realtime - Realtime and audio overview. Use first to pick the correct guide for voice agents, live translation, transcription, prompting, transports, tools, server controls, and costs.
- https://developers.openai.com/api/docs/guides/audio - Broader audio and speech guide. Use when the user may not need a full bidirectional Realtime session.
- https://developers.openai.com/api/docs/guides/voice-agents - Higher-level voice agent guide. Use for agent lifecycle, tool use, guardrails, handoffs, and session-history concepts.

## Transports

- https://developers.openai.com/api/docs/guides/realtime-webrtc - WebRTC guide. Use for browser/mobile realtime voice and direct client media sessions.
- https://developers.openai.com/api/docs/guides/realtime-websocket - WebSocket guide. Use for backend services, telephony bridges, and custom event/audio pipelines.
- https://developers.openai.com/api/docs/guides/realtime-sip - SIP guide. Use for telephony/SIP integrations.

## Session And Event References

- https://developers.openai.com/api/docs/api-reference/realtime-sessions - Session/client secret reference. Use for ephemeral token creation and session configuration fields.
- https://developers.openai.com/api/docs/api-reference/realtime_client_events - Client event reference. Use before sending `session.update`, conversation item events, response events, input audio events, or cancellation/truncation events.
- https://developers.openai.com/api/docs/api-reference/realtime_server_events - Server event reference. Use before writing event reducers, UI state machines, transcript handling, response assembly, interruption handling, or tool-call lifecycle code.

## Conversation And Turn Taking

- https://developers.openai.com/api/docs/guides/realtime-conversations - Managing conversations. Use for conversation items, response lifecycle, interruptions, truncation, and context management.
- https://developers.openai.com/api/docs/guides/realtime-vad - Voice activity detection. Use for server VAD, semantic VAD, manual turns, idle timeouts, and threshold tuning.
- https://developers.openai.com/api/docs/guides/realtime-models-prompting - Realtime prompting guide. Use for instructions that control voice behavior, turn taking, tool use, style, and robustness.

## Specialized Realtime Modes

- https://developers.openai.com/api/docs/guides/realtime-transcription - Realtime transcription. Use for speech-to-text streaming, transcription sessions, audio formats, language hints, and transcript events.
- https://developers.openai.com/api/docs/guides/realtime-translation - Live translation. Use for speech translation or multilingual realtime flows.

## Tools, MCP, And Server Controls

- https://developers.openai.com/api/docs/guides/realtime-mcp - Realtime with tools. Use for function tools, MCP tool availability, tool call events, and tool result handling.
- https://developers.openai.com/api/docs/guides/realtime-server-controls - Webhooks and server-side controls. Use for server-mediated tool calling, guardrails, webhooks, and policy controls.

## Costs And Production Readiness

- https://developers.openai.com/api/docs/guides/realtime-costs - Managing Realtime costs. Use for token/audio usage, prompt caching, context/truncation, idle sessions, and architecture cost tradeoffs.
- https://developers.openai.com/api/docs/guides/cost-optimization - General API cost optimization. Use when Realtime costs intersect with broader model, caching, or architecture choices.

## Quick Lookup Queries

Use these with the OpenAI docs MCP search when available:

- `Realtime API WebRTC client secret calls SDP`
- `Realtime API WebSocket session.update input_audio_buffer`
- `Realtime client events response.create conversation.item.create`
- `Realtime server events response.done response.output_item.done tool calls`
- `Realtime VAD semantic_vad server_vad idle timeout`
- `Realtime transcription sessions input audio transcription`
- `Realtime MCP tools server-side controls webhooks`
- `Realtime costs prompt caching truncation audio tokens`

