from abc import ABC, abstractmethod


# Handler interface
class Handler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        if self.can_handle(request):
            return self.process(request)
        elif self.next_handler:
            print(f"{self.__class__.__name__}: Can't handle request: {request}")
            return self.next_handler.handle(request)
        return f"No handler found for request: {request}"

    @abstractmethod
    def can_handle(self, request):
        pass

    @abstractmethod
    def process(self, request):
        pass


# ConcreteHandler1
class ConcreteHandler1(Handler):
    def can_handle(self, request):
        return request.startswith("Task1")

    def process(self, request):
        print(f"ConcreteHandler1: Handling request: {request}")


# ConcreteHandler2
class ConcreteHandler2(Handler):
    def can_handle(self, request):
        return request.startswith("Task2")

    def process(self, request):
        print(f"ConcreteHandler2: Handling request: {request}")


# DefaultHandler
class DefaultHandler(Handler):
    def can_handle(self, request):
        return True

    def process(self, request):
        print(f"DefaultHandler: Handling request: {request}")


# Chain Builder (optional) -> client use this to build the chain
class HandlerConfigurator:
    def __init__(self):
        self._handler_chain = self.get_handler_chain()

    @staticmethod
    def get_handler_chain():
        return ConcreteHandler1(
            ConcreteHandler2(
                DefaultHandler()
            )
        )

    def handle(self, request):
        self._handler_chain.handle(request)


# Client code
def main():
    handler_chain = HandlerConfigurator()

    handler_chain.handle("Task1")
    handler_chain.handle("Task2")
    handler_chain.handle("UnknownTask")


if __name__ == "__main__":
    main()
