from abc import ABC, abstractmethod


# Product
class Product:

    def __init__(self):
        self.a = None
        self.b = None
        self.c = None

    def __str__(self):
        return f"Product= {self.a}, {self.b}, {self.c}"


# Abstract Builder
class BaseBuilder(ABC):
    def __init__(self):
        self.product = Product()

    @abstractmethod
    def set_a(self, a):
        pass

    @abstractmethod
    def set_b(self, b):
        pass

    @abstractmethod
    def set_c(self, c):
        pass

    def get_result(self):
        return self.product


# Concrete Builder
class ConcreteBuilder(BaseBuilder):

    def set_a(self, a):
        self.product.a = a
        return self

    def set_b(self, b):
        self.product.b = b
        return self

    def set_c(self, c):
        self.product.c = c
        return self


# Director
class Director:

    def __init__(self, builder: BaseBuilder):
        self.builder = builder

    def create_product(self, a, b, c):
        self.builder.set_a(a).set_b(b).set_c(c)


# Client Code
def client_code(a, b, c):
    builder = ConcreteBuilder()
    director = Director(builder)
    director.create_product(a, b, c)
    product = builder.get_result()
    return product


def main():
    product1 = client_code('one', 'two', 'three')
    print(f'Product1: {product1}')
    product2 = client_code('four', 'five', 'six')
    print(f'Product2: {product2}')


if __name__ == "__main__":
    main()
