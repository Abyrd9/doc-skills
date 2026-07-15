---
name: electron-docs
description: Electron docs workflow for desktop app architecture, main/renderer/preload boundaries, secure IPC, BrowserWindow/webContents hardening, native integrations, packaging, signing, updates, distribution, testing, debugging, and web-to-Electron migration.
---

# Electron Docs

## Core Workflow

Start from official Electron docs before making architecture or API choices. Electron changes security defaults, platform support, and release guidance over time, so prefer live documentation over memory for anything nontrivial.

1. Identify the task lane: architecture, security, native integration, packaging/release, testing/debugging, or migration from web app.
2. Read the matching section in [references/electron-doc-map.md](references/electron-doc-map.md).
3. Open the linked official docs that apply to the task before writing code or advice.
4. Design the app around strict process boundaries: main owns lifecycle/native privileged work, renderer owns UI, preload exposes small typed APIs, and IPC channels are narrow and validated.
5. Treat security as part of the first design pass, not a cleanup step.
6. For release work, verify packaging, signing, notarization, update, and platform requirements before choosing tooling or CI steps.
7. Completion: architecture, code, or advice is grounded in the relevant official docs, with security and process-boundary implications accounted for.

## Default Electron Architecture

Prefer this baseline unless the project already has a stronger pattern:

- Main process: create windows, own app lifecycle, register native integrations, handle privileged filesystem/network/OS actions, and register IPC handlers.
- Renderer process: render UI only; do not enable direct Node or Electron access for routine UI code.
- Preload script: bridge a minimal, explicit API into the renderer with `contextBridge`.
- IPC: expose named methods such as `settings.load()` or `files.pickProject()`, not raw `ipcRenderer`, generic command dispatch, or broad filesystem APIs.
- Content loading: load local bundled assets or a controlled development URL; guard navigation and popup creation in production.
- Persistence: choose storage deliberately. Use renderer storage only for low-risk UI state; route privileged or sensitive persistence through main/preload APIs.

## Security Defaults

Before shipping or adding risky integrations:

- Keep `contextIsolation` enabled.
- Keep renderer `nodeIntegration` disabled unless there is a documented, reviewed exception.
- Keep sandboxing enabled for renderers whenever possible.
- Validate IPC senders and arguments in the main process.
- Use a Content Security Policy appropriate to the loaded content.
- Restrict navigation, `window.open`, and external URL handling.
- Avoid `<webview>` unless there is a hard product need; if used, read the official `<webview>` docs and enforce `will-attach-webview`.
- Do not expose raw Electron objects, raw Node modules, or raw event objects to renderer code.

## Web App Migration Notes

When converting an existing Vite/React/TanStack app:

- Keep the UI build as a renderer bundle and add Electron entry points rather than mixing Electron imports into shared UI components.
- Use Vite dev server only in development; load built local files in production.
- Make API/backend assumptions explicit. Decide whether the desktop app talks to a hosted service, embeds a local service, or moves capabilities into main-process handlers.
- Replace browser-only auth or callback flows with desktop-safe deep-link, external-browser, or device-code flows as appropriate.
- Check filesystem, notification, menu, tray, and protocol needs against native integration docs before implementing.

## Verification Checklist

For meaningful Electron work, verify at least:

- Development app launches and opens a window.
- Renderer works without direct Node access.
- Preload API surface is typed or otherwise explicit.
- IPC paths validate inputs and reject unauthorized senders.
- Navigation and popup policy is enforced.
- Packaged app can be built for the target platform.
- Release path documents signing/notarization/update requirements.
