from Structural.Proxy.examples.request_handler.request_handler import RequestHandler, WebAppRequestHandler


# Caching Proxy
# Usage -> for caching results of requests and reusing them later
class CachingProxy(RequestHandler):
    def __init__(self, real_handler: WebAppRequestHandler):
        self._real_handler = real_handler
        self._cache = {}

    def handle_request(self, request):
        if request in self._cache:
            print(f"CachingProxy: Returning cached result for '{request}'.")
            print(f"Cached Result: {self._cache[request]}")
        else:
            print(f"CachingProxy: Fetching new value for '{request}'.")

            result = f"Processed result for '{request}'"
            self._cache[request] = result
            self._real_handler.handle_request(request)
            print(f"CachingProxy: Result stored in cache: {result}")
