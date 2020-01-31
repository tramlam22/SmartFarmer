const CACHE_NAME = 'my-site-cache-v'; //+ new Date().getTime();
const urlsToCache = [
  'static/base.js',
];

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('saving cache');
        return cache.addAll(urlsToCache);
      }).then(()=>{
        console.log('skipWaiting');
        return self.skipWaiting();
      }) 
  );
});

self.addEventListener('activate', function(event) {
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(cacheNames
        .filter(cacheName => cacheName !== CACHE_NAME)
        .map(cacheName => caches.delete(cacheName))
      )
  	})
  );
});

self.addEventListener('fetch', function (event) {
 /*  if (event.request.redirect === "manual") {
    console.log("request redirection was manual")
    return;
  }*/
  if (event.request.method === "POST") { return;}
  function headersArr(){
    let h = [];
		event.request.headers.forEach(header=>{
      h.push(header);
    });
    return h;
  }
  console.log(headersArr());
  if (headersArr().includes('XMLHttpRequest')) {
    console.log("there was an ajax request executed");
    return;
  } else {
    event.respondWith(
    caches.match(event.request)
    .then(function (myCacheResponse) {
/*       if (myCacheResponse) {
        console.log(myCacheResponse);
        if (myCacheResponse.redirected) {
          const clonedResponse = myCacheResponse.clone();
          const bodyPromise = 'body' in clonedResponse ?
            Promise.resolve(clonedResponse.body) :
            clonedResponse.blob();
          console.log(clonedResponse.url);
          
          return bodyPromise.then((body) => {
            return new Response(body, {
              headers: clonedResponse.headers,
              status: clonedResponse.status,
              statusText: clonedResponse.statusText,
            });
          });
        }
      }  */
      if (myCacheResponse) {
        console.log("fetching from storage");
      } else {
        console.log("fetching from network");
      }
      return myCacheResponse || fetch(event.request);
    	})
  	);
  }
  
  
});


/* if (serviceWorker && django request)
then django request; */
