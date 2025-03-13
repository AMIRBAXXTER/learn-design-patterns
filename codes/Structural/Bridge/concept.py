from abc import ABC, abstractmethod


# Implementor Interface
class Implementor(ABC):

    @abstractmethod
    def operation_imp(self):
        pass


# Concrete Implementors
class ConcreteImplementorA(Implementor):

    def operation_imp(self):
        return "ConcreteImplementorA: OperationImp"


class ConcreteImplementorB(Implementor):

    def operation_imp(self):
        return "ConcreteImplementorB: OperationImp"


# Abstraction
class Abstraction(ABC):
    def __init__(self, implementor: Implementor):
        self._implementor = implementor

    @abstractmethod
    def operation(self):
        pass


# Refined Abstraction
class RefinedAbstraction(Abstraction):

    def operation(self):
        return f"RefinedAbstraction: Extended Operation with -> {self._implementor.operation_imp()}"


# Client Code
def client_code(abstraction: Abstraction):
    print(abstraction.operation())


def main():
    implementor_a = ConcreteImplementorA()
    implementor_b = ConcreteImplementorB()

    abstraction_b = RefinedAbstraction(implementor_b)
    print("Client: RefinedAbstraction with ConcreteImplementorB:")
    client_code(abstraction_b)
    print("\n")

    refined_abstraction_a = RefinedAbstraction(implementor_a)
    print("Client: RefinedAbstraction with ConcreteImplementorA:")
    client_code(refined_abstraction_a)
    print("\n")


if __name__ == "__main__":
    main()
