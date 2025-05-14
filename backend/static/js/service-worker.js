const CACHE_NAME = "kallebyevangelho-v1";
const urlsToCache = [
  "/",
  "/sobre.html",
  "/projetos.html",
  "/formulario.html",
  "/contato.html",
  "/static/css/style.css",
  "/static/js/main.js",
  "/static/img/favicon.png",
  "/offline.html"
];

// Instalando o Service Worker
self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log("Cachando arquivos");
        return cache.addAll(urlsToCache);
      })
  );
});

// Buscando recursos
self.addEventListener("fetch", event => {
  event.respondWith(
    fetch(event.request).catch(() => caches.match(event.request).then(response => {
      return response || caches.match('/offline.html');
    }))
  );
});

// Atualizando o Service Worker
self.addEventListener("activate", event => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (!cacheWhitelist.includes(cacheName)) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});