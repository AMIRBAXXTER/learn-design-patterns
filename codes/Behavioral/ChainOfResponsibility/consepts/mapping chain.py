from abc import ABC, abstractmethod


# Handler interface
class Handler(ABC):
    @abstractmethod
    def handle(self, request):
        pass


# ConcreteHandler1
class ConcreteHandler1(Handler):
    def handle(self, request):
        print(f"ConcreteHandler1: Handling request: {request}")


# ConcreteHandler2
class ConcreteHandler2(Handler):
    def handle(self, request):
        print(f"ConcreteHandler2: Handling request: {request}")


# Client code
def main():
    handlers = {"Task1": ConcreteHandler1(), "Task2": ConcreteHandler1()}

    for request in ["Task1", "Task2"]:
        handlers.get(request, ).handle(request)


if __name__ == "__main__":
    main()
