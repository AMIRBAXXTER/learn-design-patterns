from abc import ABC, abstractmethod


class BaseFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass


class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self):
        pass


class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self):
        pass


class ConcreteProductA1(AbstractProductA):
    def operation_a(self):
        return "Operation A1 executed"


class ConcreteProductA2(AbstractProductA):
    def operation_a(self):
        return "Operation A2 executed"


class ConcreteProductB1(AbstractProductB):
    def operation_b(self):
        return "Operation B1 executed"


class ConcreteProductB2(AbstractProductB):
    def operation_b(self):
        return "Operation B2 executed"


class ConcreteFactory1(BaseFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(BaseFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


def client_code(factory: BaseFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(product_a.operation_a())
    print(product_b.operation_b())


def main():
    print("Using ConcreteFactory1:")
    client_code(ConcreteFactory1())

    print("\nUsing ConcreteFactory2:")
    client_code(ConcreteFactory2())


if __name__ == "__main__":
    main()
