class Base:

    def show(self):
        print(f'a instance of class {self.__class__.__name__}')


class A(Base):
    pass


class B(Base):
    pass


class C(Base):
    pass


class SimpleFactory:
    @staticmethod
    def create(class_name):
        """match class_name:
            case 'A':
                return A()
            case 'B':
                return B()
            case 'C':
                return C()
            case _:
                raise ValueError(f'{class_name} is not a valid class name')"""

        # we can use reflection to avoid this switch case or if-else
        cases = {
            'A': A,
            'B': B,
            'C': C
        }
        if class_name in cases:
            return cases[class_name]()
        else:
            raise ValueError(f'{class_name} is not a valid class name')


def main():
    a = SimpleFactory.create('A')
    a.show()
    b = SimpleFactory.create('B')
    b.show()
    c = SimpleFactory.create('C')
    c.show()
    try:
        d = SimpleFactory.create('D')
        d.show()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
