var offline = 'offline';
var path = [
    '/dashboard/',
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
    // every request from our site, passes through the fetch handler
    event.respondWith(
        caches.match(event.request)
            .then(function (response) {
                caches.open(offline).then(function (cache) { cache.add(event.request) });
                if (response) {
                    return response;
                }
                return fetch(event.request);
            }
            ))
})
