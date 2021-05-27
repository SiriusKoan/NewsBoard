var CACHE_NAME = 'offline';
var urlsToCache = [
    '/',
    '/login',
    '/register',
    '/static/index.css',
    '/static/inputs.css',
    '/static/messages.css',
    '/static/index.js',
    '/static/msg.js',
    'https://fonts.googleapis.com/css2?family=Caveat&display=swap',
];
self.addEventListener('install', function (event) {
    // install files needed offline
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function (cache) {
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', function (event) {
    // every request from our site, passes through the fetch handler
    event.respondWith(
        // check all the caches in the browser and find out whether our request is in any of them
        caches.match(event.request)
            .then(function (response) {
                if (response) {
                    // there's a match and return the response stored in browser
                    return response;
                }
                // no match in cache, use the network instead
                return fetch(event.request);
            }
            )
    );
});
