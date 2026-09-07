---
name: expo-docs
description: Expo docs workflow for current, SDK-matched official guidance. Use for Expo SDK libraries, Expo Router, Expo CLI, app config, config plugins, Continuous Native Generation and prebuild, development builds, Expo Go, Expo Modules API, web support, EAS Build, Update, Submit, Hosting, Workflows, or upgrading an Expo project.
---

# Expo Docs

Use the installed Expo surface and current official documentation as the sources of truth. Expo APIs, SDK compatibility, Router behavior, and EAS commands change often; do not answer them from memory.

## First-party task skills

Load Expo's official [`expo-overview`](https://github.com/expo/skills/tree/main/plugins/expo/skills/expo-overview) skill first for Expo or EAS work; it routes to the matching first-party task skill. In particular:

- Use [`eas-update`](https://github.com/expo/skills/tree/main/plugins/expo/skills/eas-update) for EAS Update setup, publishing, runtime compatibility, testing, and debugging.
- Use [`eas-update-insights`](https://github.com/expo/skills/tree/main/plugins/expo/skills/eas-update-insights) for update adoption, crash rates, rollout health, and payload metrics.

Use the SDK-matched docs workflow below to verify exact APIs and versions. The task skills do not replace it as the source of truth.

## 1. Establish the project context

1. Inspect `package.json` and the lockfile for `expo`, `react-native`, `react`, `expo-router`, Expo SDK libraries, `expo-dev-client`, and EAS tooling.
2. Inspect `app.json`, `app.config.*`, `eas.json`, `metro.config.*`, `babel.config.*`, config plugins, and `ios/` or `android/` when present.
3. Identify the Expo SDK, package manager, target platforms, Router use, Expo Go or development-build workflow, native-directory ownership, and any EAS project link.
4. For an existing React Native or native app, identify whether Expo was added through Expo modules, brownfield integration, or an Expo CLI migration.

Completion criterion: the docs search is scoped to the installed Expo SDK, project shape, target platform, and local or EAS workflow involved.

## 2. Route through official Markdown docs

Start with:

- [Expo documentation for AI agents](https://docs.expo.dev/llms/)
- [Expo docs index](https://docs.expo.dev/llms.txt)

Use the index to find the smallest set of pages for the task. Fetch a page's Markdown by appending `.md` or `/index.md` to its documentation URL.

For SDK APIs, use the exact versioned SDK bundle listed on the AI documentation page. Do not invent a bundle URL for an SDK that the page does not list. For EAS, use [the EAS documentation bundle](https://docs.expo.dev/llms-eas.txt) and the exact product pages involved.

Route by owner:

- Project setup and local development: create project, development loop, app config, libraries, development builds, debugging, or local builds.
- Native generation: CNG, prebuild, config plugins, permissions, native customization, or existing React Native apps.
- Navigation and universal apps: Expo Router, linking, web, API routes, DOM components, or platform-specific modules.
- Native extensions: Expo Modules API, autolinking, module config, native views, or brownfield integration.
- Delivery: EAS Build, Update, Submit, Hosting, Workflows, credentials, app versions, channels, or store metadata.
- Upgrades: the SDK upgrade walkthrough, release notes, migration pages, and installed package compatibility.

Completion criterion: every Expo API, config key, command, SDK-compatibility claim, and EAS behavior in the work is covered by a fetched official page for the relevant version.

## 3. Resolve version and ownership conflicts

- Use `react-native-docs` for React Native-owned components, APIs, architecture, Hermes, Fabric, Turbo Modules, or platform behavior.
- Use `react-docs` for React components, Hooks, Effects, and React Compiler behavior.
- Use the owning library's docs for third-party packages.
- If current Expo docs disagree with the pinned package, inspect installed exports, types, source, and matching release notes. State the version gap.
- Treat Expo Skills as first-party implementation advice, not the API source of truth. Current docs and installed packages win.

Completion criterion: each technical claim is assigned to Expo, React Native, React, EAS, or the third-party package that owns it.

## 4. Apply and verify

- Preserve the repository's package manager and Expo workflow.
- Use the local Expo CLI rather than the deprecated global `expo-cli`.
- Use `expo install` when Expo must select an SDK-compatible package version.
- Do not run prebuild merely to answer a question. Treat `prebuild --clean` as destructive and review generated native diffs when prebuild is part of the task.
- Treat EAS commands as external actions. Before a build, update, submit, deploy, workflow run, or credential change, confirm the account, project, profile, platform, channel, and user authorization.
- Run focused tests, typecheck, lint, `expo-doctor` when compatibility changed, resolved-config inspection when config changed, and the relevant local build or app flow.

Report the Expo SDK, official pages used, checks run, and any device, native IDE, EAS, or store action left undone.
