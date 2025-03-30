from abc import ABC, abstractmethod

from Structural.Proxy.examples.request_handler import proxies


# Subject interface
class RequestHandler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass


# Concrete Subject
class WebAppRequestHandler(RequestHandler):
    def handle_request(self, request):
        print(f"WebAppRequestHandler: Processing request '{request}'.")


def main():
    # Real subject
    real_handler = WebAppRequestHandler()

    # 1. Virtual Proxy
    print("\n--- Virtual Proxy Example ---")
    virtual_proxy = proxies.VirtualProxy()
    virtual_proxy.handle_request("Load Heavy Resource")
    virtual_proxy.handle_request("Load Heavy Resource Again")

    # 2. Remote Proxy
    print("\n--- Remote Proxy Example ---")
    remote_proxy = proxies.RemoteProxy()
    remote_proxy.handle_request("Fetch Remote Data")

    # 3. Protection Proxy
    print("\n--- Protection Proxy Example ---")
    protection_proxy = proxies.ProtectionProxy(real_handler)
    protection_proxy.handle_request({"username": "guest", "data": "View Admin Panel"})
    protection_proxy.handle_request({"username": "admin", "data": "View Admin Panel"})

    # 4. Caching Proxy
    print("\n--- Caching Proxy Example ---")
    caching_proxy = proxies.CachingProxy(real_handler)
    caching_proxy.handle_request("Request Data A")
    caching_proxy.handle_request("Request Data A")
    caching_proxy.handle_request("Request Data B")


if __name__ == "__main__":
    main()
