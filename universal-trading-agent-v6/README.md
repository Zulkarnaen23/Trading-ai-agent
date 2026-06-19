# Universal Trading Agent v6

Versi ini memakai:

```text
PWA Web App
+ Desktop Install
+ Android WebView APK wrapper
+ Backend Proxy OpenAI Platform
+ Apex Trading Intelligence Team Agent
```

## Struktur

```text
web-app/          PWA installable untuk desktop dan mobile browser
android-webview/  APK wrapper yang membuka PWA
backend-proxy/    server aman untuk OpenAI API key
docs/             panduan deploy/install
.github/          GitHub Actions
```

## Arsitektur aman

```text
PWA / WebView APK
↓
Backend Proxy
↓
OpenAI Platform
```

Jangan taruh API key di frontend atau APK.

## Mulai cepat

1. Deploy `backend-proxy`.
2. Ganti `web-app/src/agent-config.js` ke URL backend.
3. Deploy `web-app` ke Vercel/Netlify/Cloudflare Pages/GitHub Pages.
4. Install PWA dari Chrome/Edge.
5. Untuk APK, ganti `WEB_APP_URL` di `android-webview/app/build.gradle.kts`, lalu build.

## Build APK dari GitHub

Buka:

```text
Actions → Build Universal Trading Agent WebView APK → Run workflow
```

APK akan muncul di artifact bernama:

```text
universal-trading-agent-webview-debug-apk
```
