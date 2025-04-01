from abc import ABC, abstractmethod


# Handler interface
class Handler(ABC):
    @abstractmethod
    def handle(self, request):
        pass


# ConcreteHandler1
class ConcreteHandler1(Handler):
    def handle(self, request):
        if "Task1" in request:
            return f"ConcreteHandler1: Handling request: {request}"


# ConcreteHandler2
class ConcreteHandler2(Handler):
    def handle(self, request):
        if "Task2" in request:
            return f"ConcreteHandler2: Handling request: {request}"


# Client code
def main():
    handlers = [ConcreteHandler1(), ConcreteHandler2()]
    request = ["Task1", "Task2"]
    responses = []
    for handler in handlers:
        response = handler.handle(request)
        if response:
            responses.append(response)
    print(responses)


if __name__ == "__main__":
    main()
