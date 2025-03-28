from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({super().operation()})"


class ConcreteDecoratorB(ConcreteDecoratorA):
    """
    a new decorator can inherit from Decorator or
    a specific one (ConcreteDecoratorA) to extend
    behavior based on design needs.
    """

    def operation(self):
        return f"ConcreteDecoratorB({super().operation()})"


def main():
    simple = ConcreteComponent()
    print("Simple:", simple.operation())

    decorated1 = ConcreteDecoratorA(simple)
    print("Decorated with ConcreteDecoratorA:", decorated1.operation())

    decorated2 = ConcreteDecoratorB(simple)
    print("Decorated with ConcreteDecoratorA and ConcreteDecoratorB:", decorated2.operation())


if __name__ == "__main__":
    main()
