from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def operation(self):
        pass


class ConcreteProduct1(Product):

    def operation(self):
        return f'result of operation for instance of {self.__class__.__name__}'


class ConcreteProduct2(Product):

    def operation(self):
        return f'result of operation for instance of {self.__class__.__name__}'


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f'Creator: using {product.operation()}'
        return result


class ConcreteCreator1(Creator):

    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):

    def factory_method(self):
        return ConcreteProduct2()


def main():
    creator1 = ConcreteCreator1()
    creator2 = ConcreteCreator2()
    print(creator1.some_operation())
    print(creator2.some_operation())


if __name__ == "__main__":
    main()
