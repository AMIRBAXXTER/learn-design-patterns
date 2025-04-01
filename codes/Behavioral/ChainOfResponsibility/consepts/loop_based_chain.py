from abc import ABC, abstractmethod


# Handler interface
class Handler(ABC):

    def handle(self, request):
        if self.can_handle(request):
            return self.process(request)
        print(f"{self.__class__.__name__}: Can't handle request: {request}")

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


# Client code
def main():
    requests = ["Task1", "Task2", "UnknownTask"]
    handlers = [ConcreteHandler1(), ConcreteHandler2()]

    for request in requests:
        for handler in handlers:
            handler.handle(request)


if __name__ == "__main__":
    main()
