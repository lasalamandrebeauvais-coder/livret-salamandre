/**
 * Service Worker pour La Salamandre v2.1
 * Caching strategy: Network-First pour dynamique, Cache-First pour les assets
 * Permet le fonctionnement hors-ligne
 */

const CACHE_VERSION = 'v2.1.0';
const CACHE_NAME = `salamandre-${CACHE_VERSION}`;
const RUNTIME_CACHE = `salamandre-runtime-${CACHE_VERSION}`;

// Assets à mettre en cache - les fichiers critiques
const CRITICAL_ASSETS = [
  '/',
  '/index.html',
  '/manifest.json',
  '/i18n.js',
  '/stephane.jpg',
  '/telephone_rouge.jpg',
  '/senteur.jpg',
  '/terrasse1.jpg',
  '/art.jpg'
];

// Événement d'installation - créer le cache initial
self.addEventListener('install', (event) => {
  console.log('Service Worker: Installation en cours...');
  
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log(`Service Worker: Cache '${CACHE_NAME}' créé`);
      
      // Mettre en cache les assets critiques
      return cache.addAll(CRITICAL_ASSETS).catch((error) => {
        console.warn('Service Worker: Impossible de mettre en cache tous les assets', error);
        // Continuer même si certains assets ne sont pas disponibles
        return cache.addAll(
          CRITICAL_ASSETS.filter(url => url === '/' || url === '/index.html' || url === '/manifest.json')
        );
      });
    })
  );
  
  // Forcer l'activation immédiate
  self.skipWaiting();
});

// Événement d'activation - nettoyer les anciens caches
self.addEventListener('activate', (event) => {
  console.log('Service Worker: Activation en cours...');
  
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME && cacheName !== RUNTIME_CACHE) {
            console.log(`Service Worker: Suppression du cache ancien '${cacheName}'`);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  
  // Prendre le contrôle immédiatement
  return self.clients.claim();
});

// Événement fetch - gestion du caching
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);
  
  // Ignorer les requêtes non-GET
  if (request.method !== 'GET') {
    return;
  }
  
  // Ignorer les requêtes externes (CDN, APIs tierces)
  if (url.origin !== location.origin) {
    event.respondWith(
      fetch(request).catch(() => {
        // Fallback silencieux si la ressource externe n'est pas disponible
        return new Response('Ressource externe indisponible', {
          status: 503,
          statusText: 'Service Unavailable'
        });
      })
    );
    return;
  }
  
  // Stratégie pour les documents HTML (Network-First)
  if (request.headers.get('accept')?.includes('text/html')) {
    event.respondWith(
      fetch(request)
        .then((response) => {
          // Mettre en cache la réponse valide
          if (response.ok) {
            const cache = caches.open(RUNTIME_CACHE);
            cache.then((c) => c.put(request, response.clone()));
          }
          return response;
        })
        .catch(() => {
          // Fallback au cache si offline
          return caches.match(request).then((cached) => {
            return cached || caches.match('/index.html');
          });
        })
    );
    return;
  }
  
  // Stratégie pour les assets (scripts, styles, images) - Cache-First
  event.respondWith(
    caches.match(request).then((cached) => {
      return cached || fetch(request)
        .then((response) => {
          // Mettre en cache les réponses valides
          if (response.ok) {
            const cache = caches.open(RUNTIME_CACHE);
            cache.then((c) => c.put(request, response.clone()));
          }
          return response;
        })
        .catch(() => {
          // Fallback pour les images manquantes
          if (request.destination === 'image') {
            return new Response(
              '<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300"><rect fill="#f0f0f0" width="400" height="300"/><text x="50%" y="50%" text-anchor="middle" dy=".3em" fill="#999" font-size="14">Image non disponible</text></svg>',
              { headers: { 'Content-Type': 'image/svg+xml' } }
            );
          }
          return new Response('Hors ligne', { status: 503 });
        })
    })
  );
});

// Gestion des messages depuis la page
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
  
  if (event.data && event.data.type === 'CLIENTS_CLAIM') {
    self.clients.claim();
  }
  
  // Notifier les clients de la mise à jour
  if (event.data && event.data.type === 'UPDATE_AVAILABLE') {
    self.clients.matchAll().then((clients) => {
      clients.forEach((client) => {
        client.postMessage({
          type: 'UPDATE_AVAILABLE',
          message: 'Une nouvelle version est disponible. Rechargez la page.'
        });
      });
    });
  }
});

// Gestion de la synchronisation en arrière-plan (optionnel - pour les notes enregistrées, etc.)
self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-guestbook') {
    // Synchroniser les notes du livre d'or quand la connexion est rétablie
    event.waitUntil(
      // À implémenter selon vos besoins
      Promise.resolve()
    );
  }
});

console.log('Service Worker chargé et prêt pour', CACHE_NAME);
