from Structural.Proxy.examples.request_handler.request_handler import RequestHandler, WebAppRequestHandler


# Virtual Proxy
# Usage -> for lazy initialization
class VirtualProxy(RequestHandler):
    def __init__(self):
        self._real_handler = None

    def handle_request(self, request):
        if self._real_handler is None:
            print("VirtualProxy: Creating the RealSubject for the first time.")
            self._real_handler = WebAppRequestHandler()
        print("VirtualProxy: Delegating request to RealSubject.")
        self._real_handler.handle_request(request)
