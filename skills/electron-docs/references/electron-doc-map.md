# Electron Official Documentation Map

Use these official Electron docs as the primary lookup map. Prefer opening the listed URLs live before making nontrivial implementation decisions.

## Start Here

- https://www.electronjs.org/docs/latest/ - Docs index and overview. Use for the current sidebar structure and top-level recommendations.
- https://www.electronjs.org/docs/latest/tutorial/tutorial-first-app - Minimal working app, `app.whenReady()`, `BrowserWindow`, local HTML loading, macOS activate behavior, and shutdown basics.
- https://www.electronjs.org/docs/latest/tutorial/process-model - Main process, renderer processes, preload scripts, and why process boundaries matter.

## Architecture And Process Boundaries

- https://www.electronjs.org/docs/latest/api/app - App lifecycle, paths, single-instance behavior, quit events, OS integration hooks.
- https://www.electronjs.org/docs/latest/api/browser-window - Window creation and security-sensitive `webPreferences`.
- https://www.electronjs.org/docs/latest/api/web-contents - Renderer lifecycle observation, navigation control, messaging, and popup/window-open handling.
- https://www.electronjs.org/docs/latest/tutorial/tutorial-preload - Preload script basics and how to expose controlled renderer APIs.
- https://www.electronjs.org/docs/latest/tutorial/ipc - IPC patterns: one-way, request/response, main-to-renderer, and preload wrappers.
- https://www.electronjs.org/docs/latest/tutorial/context-isolation - Isolated worlds, `contextBridge`, and safe API exposure.

## Security And Hardening

- https://www.electronjs.org/docs/latest/tutorial/security - Central security checklist; read before building real features.
- https://www.electronjs.org/docs/latest/tutorial/sandbox - Renderer sandbox behavior, defaults, and Node integration tradeoffs.
- https://www.electronjs.org/docs/latest/api/context-bridge - What can cross from preload to renderer, proxy/freeze semantics, and dangerous exposure patterns.
- https://www.electronjs.org/docs/latest/api/ipc-renderer/ - Renderer IPC API and warnings about exposing event objects.
- https://www.electronjs.org/docs/latest/api/session - Permission handlers, sessions, partitions, cookies, cache, proxy, and protocol-related controls.
- https://www.electronjs.org/docs/latest/api/webview-tag - Required if using `<webview>`; Electron recommends avoiding it when possible.
- https://www.electronjs.org/docs/latest/api/protocol - Custom protocols, privileged schemes, and secure resource loading.
- https://www.electronjs.org/docs/api/window-open/ - `window.open`, `target=_blank`, inherited security preferences, and `setWindowOpenHandler()`.

## Native Desktop Integration

- https://www.electronjs.org/docs/latest/tutorial/menus - Practical menu guide, roles, accelerators, context menus, tray menus, and dock menus.
- https://www.electronjs.org/docs/latest/api/menu - Menu API reference.
- https://www.electronjs.org/docs/latest/api/tray - System tray/status item behavior.
- https://www.electronjs.org/docs/latest/api/dialog - Native open/save/message/error dialogs.
- https://www.electronjs.org/docs/latest/api/shell - Open files, URLs, folders, trash, and shortcuts via OS handlers.
- https://www.electronjs.org/docs/latest/api/notification - Native notification API and platform constraints.
- https://www.electronjs.org/docs/latest/tutorial/notifications - Practical notifications guide.
- https://www.electronjs.org/docs/latest/api/global-shortcut - Shortcuts that work when the app is unfocused.
- https://www.electronjs.org/docs/latest/tutorial/keyboard-shortcuts - Accelerator strings and menu vs global shortcut decisions.
- https://www.electronjs.org/docs/latest/tutorial/native-file-drag-drop - Drag files from Electron into native apps/file managers.
- https://www.electronjs.org/docs/latest/tutorial/launch-app-from-url-in-another-app - Deep links and custom protocol launch flows.
- https://www.electronjs.org/docs/latest/api/utility-process - Isolate Node scripts in Chromium child processes.
- https://www.electronjs.org/docs/latest/tutorial/multithreading - Worker threads and native module caveats.
- https://www.electronjs.org/docs/latest/tutorial/using-native-node-modules - Native `.node` modules, ABI issues, and `@electron/rebuild`.

## Platform Polish

- https://www.electronjs.org/docs/latest/tutorial/recent-documents - Windows Jump Lists and macOS recent documents.
- https://www.electronjs.org/docs/latest/tutorial/windows-taskbar - Windows taskbar progress, overlays, thumbnail toolbars, Jump Lists, and attention requests.
- https://www.electronjs.org/docs/latest/tutorial/linux-desktop-actions - Linux desktop launcher actions.

## Packaging, Distribution, And Updates

- https://www.electronjs.org/docs/latest/tutorial/distribution-overview - Production release map: packaging, signing, publishing, app stores, updates.
- https://www.electronjs.org/docs/latest/tutorial/forge-overview - Electron Forge as the recommended high-level packaging/publishing path.
- https://www.electronjs.org/docs/latest/tutorial/tutorial-packaging - Practical Forge packaging and make flow.
- https://www.electronjs.org/docs/latest/tutorial/application-distribution - Prebuilt binaries, `app.asar`, resources layout, and app rebranding.
- https://www.electronjs.org/docs/latest/tutorial/code-signing - macOS signing/notarization and Windows signing guidance.
- https://www.electronjs.org/docs/latest/tutorial/updates - Auto-update design and update feed patterns.
- https://www.electronjs.org/docs/latest/api/auto-updater - `autoUpdater` API, platform support, events, feed URL, update install flow.
- https://www.electronjs.org/docs/latest/tutorial/mac-app-store-submission-guide - Mac App Store signing, sandbox entitlements, MAS build limits, and disabled modules.
- https://www.electronjs.org/docs/latest/tutorial/installation - Supported platforms/architectures and binary install/download troubleshooting.

## Quality, Performance, And Maintenance

- https://www.electronjs.org/docs/latest/tutorial/performance - Startup, memory, CPU, renderer responsiveness, main-process blocking, bundling, and profiling checklist.
- https://www.electronjs.org/docs/latest/tutorial/electron-timelines - Support policy and upgrade planning; use for security/update cadence.
- https://www.electronjs.org/docs/latest/tutorial/debugging-main-process - Debugging the main process.
- https://www.electronjs.org/docs/latest/tutorial/devtools-extension - DevTools extension usage.
- https://www.electronjs.org/docs/latest/tutorial/testing-on-headless-ci - Headless CI testing guidance.

