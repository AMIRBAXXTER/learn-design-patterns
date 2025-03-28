from abc import ABC, abstractmethod


# Component
class RequestHandler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass


# ConcreteComponent
class BasicRequestHandler(RequestHandler):
    def handle_request(self, request):
        return f"Request '{request}' processed."


# Decorator
class RequestHandlerDecorator(RequestHandler):
    def __init__(self, handler: RequestHandler):
        self._handler = handler

    def handle_request(self, request):
        return self._handler.handle_request(request)


# ConcreteDecoratorA
class LoggingRequestHandler(RequestHandlerDecorator):
    def handle_request(self, request):
        print(f"[LOG] Handling request: {request}")
        response = super().handle_request(request)
        print(f"[LOG] Request handled successfully.")
        return response


# ConcreteDecoratorB
class AuthenticationRequestHandler(RequestHandlerDecorator):
    def __init__(self, handler, valid_token):
        super().__init__(handler)
        self._valid_token = valid_token

    def handle_request(self, request):
        token = request.get("token")
        if token != self._valid_token:
            return "Unauthorized request."
        return super().handle_request(request)


# ConcreteDecoratorC
class CompressionRequestHandler(RequestHandlerDecorator):
    def handle_request(self, request):
        response = super().handle_request(request)
        return f"Compressed[{response}]"


def main():
    basic_handler = BasicRequestHandler()
    logging_handler = LoggingRequestHandler(basic_handler)
    auth_handler = AuthenticationRequestHandler(logging_handler, valid_token="VALID_TOKEN")
    full_handler = CompressionRequestHandler(auth_handler)
    request = {"data": "Get user info", "token": "VALID_TOKEN"}
    print(full_handler.handle_request(request))


if __name__ == "__main__":
    main()
