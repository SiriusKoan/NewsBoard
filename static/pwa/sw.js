const offline = 'offline_cache';
const path = [
    '/dashboard/',
    '/static/icon.png',
    '/static/index.css',
    '/static/inputs.css',
    '/static/messages.css',
    '/static/dashboard.css',
    '/static/index.js',
    '/static/msg.js',
    '/static/bg/index.jpg',
    '/static/bg/form.jpg',
    '/static/bg/dashboard.jpg',
    'https://fonts.googleapis.com/css2?family=Caveat&display=swap',
];
self.addEventListener('install', function (event) {
    // install files needed offline
    event.waitUntil(
        caches.open(offline)
            .then(function (cache) {
                return cache.addAll(path);
            }),
    );
});

self.addEventListener('fetch', function (event) {
    caches.match(event.request).then(function (response) {
        if (navigator.onLine & response) {
            // refresh caches when online
            caches.open(offline).then(function (cache) { cache.add(event.request) });
        }
    }
    )
    event.respondWith(
        caches.match(event.request).then(function (response) {
            if (response) {
                return response;
            }
            else {
                return fetch(event.request);
            }
        }
        ))
})
