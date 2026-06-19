# Install di Android

## Opsi 1 — PWA dari Chrome

1. Buka URL web app di Chrome Android.
2. Klik menu titik tiga.
3. Pilih Add to Home Screen / Install App.

## Opsi 2 — WebView APK

1. Deploy web-app ke domain HTTPS.
2. Edit:

```text
universal-trading-agent-v6/android-webview/app/src/main/res/values/strings.xml
```

Ganti:

```xml
<string name="web_app_url">https://YOUR-PWA-DOMAIN.example.com</string>
```

3. Build APK dari GitHub Actions:

```text
Actions → Build Universal Trading Agent WebView APK → Run workflow
```

4. Download artifact APK dan install di Android.
