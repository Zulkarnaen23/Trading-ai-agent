# Backend Proxy v6

Backend ini menjaga agar OpenAI API key tidak berada di frontend/PWA/APK.

```text
PWA / WebView APK
↓
Backend Proxy
↓
OpenAI Platform
```

## Jalankan lokal

```bash
cd backend-proxy
npm install
cp .env.example .env
```

Isi `.env`:

```text
OPENAI_API_KEY=your-openai-api-key-here
OPENAI_MODEL=gpt-5.5
PORT=3000
```

Jalankan:

```bash
npm start
```
