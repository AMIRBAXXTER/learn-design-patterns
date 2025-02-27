from concept import Base


class Square(Base):

    def __init__(self, side):
        self.side = side


class Circle(Base):

    def __init__(self, radius):
        self.radius = radius


class Triangle(Base):

    def __init__(self, sides):
        self.side1 = sides[0]
        self.side2 = sides[1]
        self.side3 = sides[2]


script_cases = {
    'Square': Square,
    'Circle': Circle,
    'Triangle': Triangle
}


class SimpleFactory:
    """
    this factory can create any class that is in script_cases,
    and we can use this class  in any script
    """

    def __init__(self, cases):
        self.cases = cases

    def create(self, class_name, *args, **kwargs):
        if class_name in self.cases:
            return self.cases[class_name](*args, **kwargs)
        else:
            raise ValueError(f'{class_name} is not a valid class name')


def main():
    factory = SimpleFactory(script_cases)
    a = factory.create('Square', 10)
    a.show()
    b = factory.create('Circle', 5)
    b.show()
    c = factory.create('Triangle', (10, 10, 10))
    c.show()
    try:
        d = factory.create('Dot')
        d.show()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
