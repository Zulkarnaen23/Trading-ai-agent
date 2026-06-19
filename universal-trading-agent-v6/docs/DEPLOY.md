# Deploy v6

## Backend

```bash
cd universal-trading-agent-v6/backend-proxy
npm install
cp .env.example .env
npm start
```

Deploy backend ke Render/Railway/Fly/VPS.

## Web App

Deploy folder:

```text
universal-trading-agent-v6/web-app
```

ke:

- Vercel
- Netlify
- Cloudflare Pages
- GitHub Pages

Setelah deploy, edit:

```text
universal-trading-agent-v6/web-app/src/agent-config.js
```

Ganti `proxyUrl` ke URL backend kamu.

## Android WebView

Edit:

```text
universal-trading-agent-v6/android-webview/app/src/main/res/values/strings.xml
```

Ganti `web_app_url` ke URL PWA kamu.
