from Creational.Singleton.concept import BaseClass


class MultitonMeta(type):
    """
    use this metaclass to create multiton class
    """
    _instance = {}

    def __call__(cls, key, *args, **kwargs):
        if key not in cls._instance:
            cls._instance[key] = super(MultitonMeta, cls).__call__(key, *args, **kwargs)
        return cls._instance[key]


class Multiton(BaseClass, metaclass=MultitonMeta):
    def __init__(self, key):
        super().__init__(key)


class MultitonClass(BaseClass):
    _instance = {}

    def __new__(cls, key, *args, **kwargs):
        if key not in cls._instance:
            cls._instance[key] = super(MultitonClass, cls).__new__(cls)
        return cls._instance[key]

    def __init__(self, key):
        super().__init__(key)


def multiton(cls):
    cls._instance = {}

    def get_instance(key, *args, **kwargs):
        if key not in cls._instance:
            cls._instance[key] = cls(key, *args, **kwargs)
        return cls._instance[key]

    return get_instance


@multiton
class MultitonDecorator(BaseClass):
    def __init__(self, key):
        super().__init__(key)


def decorator_multiton():
    print('decorator multiton infos')
    s5 = MultitonDecorator(5)
    s6 = MultitonDecorator(5)
    s5.show_id('s5')
    s6.show_id('s6')
    print(f'is s5 == s6: {s5 is s6}')


def metaclass_multiton():
    print('metaclass multiton infos')
    s1 = Multiton(1)
    s2 = Multiton(1)
    s1.show_id('s1')
    s2.show_id('s2')
    print(f'is s1 == s2: {s1 is s2}')


def class_multiton():
    print('class multiton infos')
    s3 = MultitonClass(3)
    s4 = MultitonClass(2)
    s3.show_id('s3')
    s4.show_id('s4')
    print(f'is s3 == s4: {s3 is s4}')


if __name__ == "__main__":
    metaclass_multiton()
    print('*' * 25)
    class_multiton()
    print('*' * 25)
    decorator_multiton()
