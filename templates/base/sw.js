/* eslint-disable no-undef */
// This is the service worker with the combined offline experience (Offline page + Offline copy of pages)

const CACHE = "dev";
importScripts(
  "https://storage.googleapis.com/workbox-cdn/releases/5.1.2/workbox-sw.js"
);

self.__WB_DISABLE_DEV_LOGS = true;

const offlineFallbackPage = "/offline";

workbox.core.skipWaiting();

workbox.core.clientsClaim();

workbox.precaching.precacheAndRoute(self.__WB_MANIFEST);

self.addEventListener("install", async (event) => {
  event.waitUntil(
    caches.open(CACHE).then((cache) => cache.add(offlineFallbackPage))
  );
});

if (workbox.navigationPreload.isSupported()) {
  workbox.navigationPreload.enable();
}

workbox.routing.registerRoute(
  /\.(?:png|gif|jpg|jpeg|webp|svg)$/,
  new workbox.strategies.CacheFirst({
    cacheName: "images-cache",
    plugins: [
      new workbox.expiration.ExpirationPlugin({
        maxEntries: 60,
        maxAgeSeconds: 30 * 24 * 60 * 60,
      }),
    ],
  })
);

workbox.routing.registerRoute(
  //cache .css files
  /\.css$/,
  new workbox.strategies.CacheFirst({
    cacheName: "css-cache",
    plugins: [
      new workbox.expiration.ExpirationPlugin({
        maxEntries: 60,
        maxAgeSeconds: 30 * 24 * 60 * 60,
      }),
    ],
  })
);

workbox.routing.registerRoute(
  new RegExp("https://res.cloudinary.com/dodcxvbqu/image/upload/v1/media/"),
  new workbox.strategies.CacheFirst({
    cacheName: "media-images-cache",
    plugins: [
      new workbox.expiration.ExpirationPlugin({
        maxEntries: 50,
        maxAgeSeconds: 60 * 60 * 24 * 24,
      }),
    ],
  })
);

workbox.routing.registerRoute(
  new RegExp("https://res.cloudinary.com/dodcxvbqu/image/upload/v1/profiles/"),
  new workbox.strategies.StaleWhileRevalidate({
    cacheName: "media-images-cache",
    plugins: [
      new workbox.expiration.ExpirationPlugin({
        maxEntries: 50,
        maxAgeSeconds: 60 * 60 * 24 * 24,
      }),
    ],
  })
);

workbox.routing.registerRoute(
  new RegExp("https://files.redodevelopers.site"),
  new workbox.strategies.CacheFirst({
    cacheName: "file-cache",
    plugins: [
      new workbox.expiration.ExpirationPlugin({
        maxEntries: 50,
        maxAgeSeconds: 60 * 60,
      }),
    ],
  })
);

self.addEventListener("fetch", (event) => {
  if (event.request.mode === "navigate") {
    event.respondWith(
      (async () => {
        try {
          const preloadResp = await event.preloadResponse;

          if (preloadResp) {
            return preloadResp;
          }

          const networkResp = await fetch(event.request);
          return networkResp;
        } catch (error) {
          const cache = await caches.open(CACHE);
          const cachedResp = await cache.match(offlineFallbackPage);
          return cachedResp;
        }
      })()
    );
  }
});

self.addEventListener("push", function (event) {
  let payload = event.data
    ? event.data.text()
    : JSON.stringify({
        head: "No Content",
        body: "No Content",
        icon: "/logo.svg",
        badge: "/badge.png",
      });
  let data = JSON.parse(payload);
  let head = data.head;
  let body = data.body;
  let icon = data.icon;
  let badge = data.badge;
  let url = data.url ? data.url : self.location.origin;
  event.waitUntil(
    self.registration.showNotification(head, {
      body: body,
      icon: icon,
      badge: badge,
      data: { url: url },
    })
  );
});
self.addEventListener("notificationclick", function (event) {
  event.waitUntil(
    event.preventDefault(),
    event.notification.close(),
    self.clients.openWindow(event.notification.data.url)
  );
});
