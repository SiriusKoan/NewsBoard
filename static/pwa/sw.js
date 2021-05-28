var websites_cache = 'websites';
var websites = [
    '/dashboard/',
];
var static_files_cache = "static_files"
var static_files = [
    '/static/index.css',
    '/static/inputs.css',
    '/static/messages.css',
    '/static/index.js',
    '/static/msg.js',
    'https://fonts.googleapis.com/css2?family=Caveat&display=swap',
]
self.addEventListener('install', function (event) {
    // install files needed offline
    event.waitUntil(
        caches.open(websites_cache)
            .then(function (cache) {
                return cache.addAll(websites);
            }),
        caches.open(static_files_cache)
            .then(function (cache) {
                return cache.addAll(static_files);
            })
    );
});

self.addEventListener('fetch', function (event) {
    // every request from our site, passes through the fetch handler
    event.respondWith(
        caches.match(event.request)
            .then(function (response) {
                caches.open(websites_cache).then(function (cache) { cache.add(event.request) });
                if (response) {
                    return response;
                }
                return fetch(event.request);
            }
            ))
})
