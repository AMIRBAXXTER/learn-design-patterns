from Structural.Proxy.examples.request_handler.request_handler import RequestHandler, WebAppRequestHandler


# Protection Proxy
# Usage -> for authentication client before sending request to real subject
class ProtectionProxy(RequestHandler):
    def __init__(self, real_handler: WebAppRequestHandler):
        self._real_handler = real_handler
        self._allowed_users = {"admin"}

    def handle_request(self, request):
        username = request.get("username")
        if username not in self._allowed_users:
            print(f"ProtectionProxy: Access denied for user '{username}'.")
        else:
            print(f"ProtectionProxy: Access granted for user '{username}'.")
            self._real_handler.handle_request(request.get("data"))
