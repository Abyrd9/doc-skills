# Capacitor Docs Route Map

Use this map after the version gate in `SKILL.md`. Replace `/docs` with `/docs/vN` when the project is pinned to major `N`.

## Version and Discovery

- Current docs root: `https://capacitorjs.com/docs`
- Versioned docs: `https://capacitorjs.com/docs/v7`, `https://capacitorjs.com/docs/v6`, and older majors exposed by the docs version switcher.
- Package source of truth: installed `@capacitor/core` major in `package.json` or lockfile.
- If a versioned page warns that it is no longer actively maintained, use it only for a project pinned to that major.

## Start, Convert, and Workflow

- New or existing web app setup: `/getting-started`
- Environment prerequisites: `/getting-started/environment-setup`
- Web app build/sync/run/release loop: `/basics/workflow`
- App configuration overview: `/basics/configuring-your-app`
- Full config reference: `/config`
- JavaScript runtime helpers: `/basics/utilities`
- Web/PWA behavior: `/web`

## CLI

- CLI overview and command list: `/cli`
- Add native platforms: `/cli/commands/add`
- Copy web assets/config: `/cli/commands/copy`
- Sync web assets and native dependencies: `/cli/commands/sync`
- Run on devices/simulators: `/cli/commands/run`
- Build signed native artifacts: `/cli/commands/build`
- Open native IDEs: `/cli/commands/open`
- Update native platform dependencies: `/cli/commands/update`

Read the specific command page before using options. `run` performs `sync`; `sync` performs `copy` then `update`; `copy` is enough only when web assets or Capacitor config changed.

## Native Platforms

- iOS overview and support: `/ios`
- iOS configuration, permissions, capabilities, app rename, iPadOS caveats: `/ios/configuration`
- Custom native iOS code: `/ios/custom-code`
- iOS privacy manifest: `/ios/privacy-manifest`
- App Store deployment: `/ios/deploying-to-app-store`
- iOS troubleshooting: `/ios/troubleshooting`
- Android overview and support: `/android`
- Android configuration, permissions, icons, splash, build variables: `/android/configuration`
- Custom native Android code: `/android/custom-code`
- Android target SDK: `/android/setting-target-sdk`
- Google Play deployment: `/android/deploying-to-google-play`
- Android troubleshooting: `/android/troubleshooting`

## Plugins and Native APIs

- Plugin overview: `/plugins`
- Official plugin list and version tags: `/apis`
- Specific official plugin API: `/apis/<plugin-slug>`, for example `/apis/status-bar`, `/apis/keyboard`, `/apis/app`, `/apis/browser`, `/apis/push-notifications`, `/apis/share`, `/apis/preferences`, `/apis/filesystem`, `/apis/camera`.
- Community plugin discovery: `/plugins/community`
- Custom plugin development overview: `/plugins/creating-plugins`
- Plugin method types: `/plugins/method-types`

For official plugins, match plugin install tags to the Capacitor core major. The docs describe `latest` for newest and `latest-X` for the newest official plugin compatible with Capacitor major `X`.

## Common Guides

- Live reload: `/guides/live-reload`
- Security: `/guides/security`
- Deep links: `/guides/deep-links`
- Splash screens and icons: `/guides/splash-screens-and-icons`
- Push notifications with Firebase: `/guides/push-notifications-firebase`
- Environment-specific configurations: `/guides/environment-specific-configurations`
- CI/CD: `/guides/ci-cd`
- App deployment and realtime updates: `/guides/deploying-updates`
- Storage: `/guides/storage`
- React hooks helpers: `/guides/react-hooks`
- Mocking plugins: `/guides/mocking-plugins`

## Migration and Upgrades

- Cordova/PhoneGap overview: `/cordova`
- Cordova migration strategy: `/cordova/migrating-strategy`
- Cordova to Capacitor migration: `/cordova/migrating-from-cordova-to-capacitor`
- Major upgrade guide: `/updating/<major>-0`, for example `/updating/8-0`
- Official plugin upgrade guide: `/updating/plugins/<major>-0`, for example `/updating/plugins/8-0`

When upgrading, read both the core major upgrade guide and the plugin upgrade guide, then verify `@capacitor/core`, `@capacitor/ios`, `@capacitor/android`, and official plugins are on compatible majors.
