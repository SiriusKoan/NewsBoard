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
    var response;
    var cachedResponse = caches.match(event.request).catch(function () {
        return fetch(event.request);
    }).then(function (r) {
        response = r;
        caches.open(offline).then(function (cache) {
            if (response) {
                cache.put(event.request, response);
            }
        });
        return response.clone();
    }).catch(function () {
        return caches.match(event.request);
    });
})
