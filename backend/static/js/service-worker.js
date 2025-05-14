const CACHE_NAME = "kallebyevangelho-v2";
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

// Instalando o Service Worker e cacheando recursos
self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log("[Service Worker] Cachando novos recursos");
        return cache.addAll(urlsToCache);
      })
  );
  self.skipWaiting(); // Força ativação imediata após instalação
});

// Ativando o Service Worker e limpando caches antigos
self.addEventListener("activate", event => {
  console.log("[Service Worker] Ativando novo Service Worker...");
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            console.log("[Service Worker] Deletando cache antigo:", cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim(); // Faz o SW assumir imediatamente todas abas
});

// Interceptando fetch
self.addEventListener("fetch", event => {
  if (event.request.method !== 'GET') return; // Só tratar GETs
  event.respondWith(
    caches.match(event.request)
      .then(cachedResponse => {
        if (cachedResponse) {
          return cachedResponse; // Retorna cache
        }
        return fetch(event.request)
          .then(response => {
            return caches.open(CACHE_NAME)
              .then(cache => {
                // Atualiza cache dinamicamente para novas páginas
                cache.put(event.request, response.clone());
                return response;
              });
          });
      })
      .catch(() => caches.match('/offline.html'))
  );
});