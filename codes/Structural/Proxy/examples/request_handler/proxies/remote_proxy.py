from Structural.Proxy.examples.request_handler.request_handler import RequestHandler


# Remote Proxy
# Usage -> for sending requests to remote server and getting response
class RemoteProxy(RequestHandler):
    def handle_request(self, request):
        print(f"RemoteProxy: Sending request '{request}' to the remote server...")
        # sending request to remote server simulation
        response = f"(Server Response) Processed request: '{request}'"
        print(f"RemoteProxy: Received response from server: {response}")
