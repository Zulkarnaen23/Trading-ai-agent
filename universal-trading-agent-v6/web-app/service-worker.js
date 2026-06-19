const CACHE_NAME = "universal-trading-agent-v6";
const APP_SHELL = [
  "./",
  "./index.html",
  "./src/style.css",
  "./src/app.js",
  "./src/agent-config.js",
  "./manifest.webmanifest",
  "./icons/icon.svg"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(APP_SHELL))
  );
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(self.clients.claim());
});
