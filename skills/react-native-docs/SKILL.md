---
name: react-native-docs
description: React Native docs workflow for version-matched core components, APIs, styles, accessibility, testing, performance, platform behavior, native integration, New Architecture, Turbo Native Modules, Fabric, Codegen, Hermes, and React Native upgrades. Use expo-docs instead for Expo SDK libraries, Router, CLI, app config, prebuild, Expo Modules, or EAS.
---

# React Native Docs

Use official React Native docs and the project's installed package surface as the sources of truth. React Native docs are versioned, so establish the local version before choosing an API or command.

## First-party task skills

For a React Native version upgrade, use the React Native Community's official [`upgrade-react-native`](https://github.com/react-native-community/skills/tree/main/upgrade-react-native) skill before the docs workflow. For React Native 0.80+ Strict TypeScript API migration, use its official [`migrate-to-strict-api`](https://github.com/react-native-community/skills/tree/main/migrate-to-strict-api) skill. Then verify the result against the exact installed and target versions below.

## 1. Establish the local React Native context

1. Inspect `package.json` and the lockfile for `react-native`, `react`, Expo, the React Native Community CLI, and relevant native libraries.
2. Inspect `app.json`, `app.config.*`, `metro.config.*`, `babel.config.*`, `ios/`, `android/`, and codegen settings when present.
3. Identify the package manager, React Native version, Expo SDK when used, target platforms, framework or bare setup, and whether native folders are generated or owned by the repo.
4. Check whether the task touches the New Architecture, Hermes, Codegen, a native module, a Fabric component, or legacy native APIs.

Completion criterion: the docs search is scoped to the installed React Native version, project type, architecture, and target platform.

## 2. Route through the official docs

Start with:

- [React Native versions](https://reactnative.dev/versions)
- [React Native docs index for agents](https://reactnative.dev/llms.txt)

Use the versions page to select docs for the installed minor. Use unversioned `/docs/...` pages only for the current stable release or when no project version exists. Use `next` docs only when the user asks about an unreleased version.

Choose the smallest page set that covers the task:

- Setup and project shape: environment setup, framework guidance, getting started without a framework, or integration with existing apps.
- UI and platform behavior: the exact Core Component or API page, styles, Flexbox, touch handling, platform-specific code, accessibility, or permissions.
- Development and quality: debugging, testing, performance, build speed, security, or publishing guidance.
- Native work: Native Platform, Turbo Native Modules, Fabric Native Components, Codegen, C++, Android, or iOS pages for the installed architecture.
- Upgrades: versions, release notes, the official upgrading guide, and Upgrade Helper for the exact source and target versions.

Completion criterion: each React Native API, prop, config value, native step, or CLI command in the answer is covered by a fetched official page for the selected version.

## 3. Respect source ownership

- Use `react-docs` when the question is about React components, Hooks, Effects, Suspense, or React Compiler behavior rather than React Native.
- Use `expo-docs` for Expo Router, EAS, config plugins, prebuild, Expo modules, or SDK-owned APIs. Keep the React Native docs for the underlying React Native behavior.
- Use the owning library's docs for community packages. React Native's package directory can help discovery, but it does not replace a library's API docs.
- Prefer New Architecture docs when the installed version and project use it. Do not suggest legacy native APIs without confirming that the project still needs them.
- If the current official docs and installed types or source disagree, follow the pinned package surface and call out the version gap.

Completion criterion: each claim comes from the project, React Native, React, Expo, or a community library according to who owns that behavior.

## 4. Apply and verify

- Preserve the project's framework, package manager, native folder policy, architecture, and platform conventions unless the task changes them.
- Prefer package-provided TypeScript types and existing native templates.
- Keep iOS and Android steps distinct when their files, tools, permissions, or lifecycle differ.
- Run the repository's focused tests, typecheck, lint, and native build or app flow that matches the change.
- For UI or device behavior, verify on the affected simulator, emulator, or device when practical.
- For upgrades, inspect template diffs and release notes before changing generated native files.

Report the selected React Native version, official pages used, checks run, and any platform verification left to the user.
