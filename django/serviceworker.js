const CACHE_NAME = 'my-site-cache-v1';
const urlsToCache = [
    '/',
    '/static/css/base.css',
];

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('saving cache');
        return cache.addAll(urlsToCache);
      }).then(function(){
        console.log('skipWaiting');
        return self.skipWaiting();
      }) 
  );
});

self.addEventListener('activate', function(event) {
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
				cacheNames.filter(function(cacheName){

        }).map(function(cacheName){
          return caches.delete(cacheName);
        })
      )
  	})
  );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request).then(function(response) {
          return fetch(event.request)
          .catch(function(rsp) {
             return response; 
          });
          
        })
    );
});