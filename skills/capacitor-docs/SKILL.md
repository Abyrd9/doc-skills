---
name: capacitor-docs
description: Capacitor official docs workflow for building, migrating, configuring, debugging, or reviewing Capacitor apps. Use when Capacitor, @capacitor/* packages, cap CLI commands, capacitor.config.*, web-view-first mobile packaging, native iOS/Android project sync, plugins, live reload, app-store builds, or Cordova-to-Capacitor migration are mentioned.
---

# Capacitor Docs

Use current official Capacitor docs as the source of truth. Capacitor changes across major versions, so do not answer from memory when commands, platform support, config keys, plugins, or native project behavior matter.

## First-party task skills

Before the docs workflow, check [Ionic's Capacitor skills](https://github.com/ionic-team/capacitor-skills) for these exact tasks:

- creating a Capacitor plugin;
- migrating a Cordova plugin;
- generating OutSystems Developer Cloud build actions; or
- migrating a Capacitor 8.4 app to the 8.5 UIScene lifecycle.

Use the matching first-party skill for its workflow, then verify changing APIs and commands against the version-matched docs below. The pack does not replace this general docs workflow outside those four tasks.

## Workflow

1. Version gate the task.
   - Inspect the project for `@capacitor/core`, `@capacitor/ios`, `@capacitor/android`, official `@capacitor/*` plugins, `capacitor.config.*`, and `ios/` or `android/` native folders.
   - Use the docs major that matches `@capacitor/core` when it is installed.
   - Use the current unversioned docs only when the project is not pinned or the task is planning a new install.
   - Completion criterion: the chosen docs base is either the installed Capacitor major or the live current version.

2. Route to the smallest official docs set.
   - Read [references/route-map.md](references/route-map.md) for page selection.
   - Fetch the selected `https://capacitorjs.com/docs...`, `https://capacitorjs.com/docs/apis...`, or `https://capacitorjs.com/docs/cli...` pages live before giving detailed guidance or editing code.
   - Completion criterion: every command, config key, plugin API, or platform-specific claim in the answer is covered by a fetched official page.

3. Fit the docs to the local project.
   - Translate npm examples to the detected package manager when needed, preserving package names and Capacitor CLI semantics.
   - Check the web build output path against `webDir` before suggesting `cap copy`, `cap sync`, or native runs.
   - Treat generated native projects as real app projects; use Xcode/Android Studio docs routes for changes that live under `ios/` or `android/`.
   - Completion criterion: suggested files and commands match the local framework, package manager, build output, and native platform folders.

4. Separate web concerns from native concerns.
   - For UI, routing, auth, API calls, and responsive behavior, inspect the web framework first.
   - For permissions, status bars, splash screens, deep links, push, app lifecycle, files, camera, share sheets, or other device APIs, read the relevant Capacitor plugin and platform pages.
   - Completion criterion: the implementation plan says which behavior stays in web code and which behavior requires Capacitor config, a plugin, or native project edits.

5. Verify through the Capacitor loop.
   - Build the web app before `cap copy` or `cap sync` unless live reload is intentionally configured.
   - Use `cap sync` after package/plugin/native dependency changes.
   - Use `cap copy` when only web assets or Capacitor config need to be copied.
   - Run the target platform or explain why local native verification was not possible.
   - Completion criterion: the final response names the docs pages consulted, the local verification performed, and any native IDE/app-store step left to the user.

## Source Policy

- Prefer official Capacitor docs and official plugin API pages.
- Use Ionic docs only when the Capacitor docs route explicitly points there, such as Ionic CLI live reload details.
- Use community plugin docs only for that plugin, and label them as community-maintained.
- Do not use older version docs when the page says that major is no longer actively maintained unless the project is pinned to that major.
- If official docs and installed package types disagree, inspect installed package types/source and call out the mismatch.

## Output Rules

- Cite or link the official Capacitor pages used when answering docs-dependent questions.
- State the selected Capacitor major when version differences matter.
- Keep setup commands exact and project-local; avoid global installs unless the docs route requires them and no local alternative fits.
- Warn before recommending production use of `server.url`, `cleartext`, or broad WebView navigation allowances.
