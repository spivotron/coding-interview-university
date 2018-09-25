import socket


class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host): # allows us to use the class like a function resolver('google.com')
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]
    def clear(self):
        self._cache.clear()
    def has_host(self, host):
        return host in self._cache
