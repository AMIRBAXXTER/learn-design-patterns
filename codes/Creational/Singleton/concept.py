class SingletonMeta(type):
    """
    use this metaclass to create singleton class
    """
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class BaseClass:
    """
    base class for singleton
    """

    def __init__(self, value):
        self.value = value

    def show_id(self, variable_name):
        print(f'{variable_name} id: {id(self)}')


class Singleton(BaseClass, metaclass=SingletonMeta):
    """
    singleton class using metaclass
    """

    def __init__(self, value):
        super().__init__(value)


class SingletonClass(BaseClass):
    """
    singleton class using __new__ and __init__
    """
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonClass, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not self._initialized:
            super().__init__(value)
            self._initialized = True


def singleton(cls):
    """
    singleton decorator
    """
    cls._instance = None
    cls._initialized = False

    def get_instance(*args, **kwargs):
        if cls._instance is None:
            cls._instance = cls(*args, **kwargs)
        return cls._instance

    return get_instance


@singleton
class SingletonDecorator(BaseClass):
    """
    singleton class using decorator
    """

    def __init__(self, value):
        super().__init__(value)


def metaclass_singleton():
    print('metaclass singleton infos')
    s1 = Singleton(1)
    s2 = Singleton(2)
    s1.show_id('s1')
    s2.show_id('s2')
    print(f'is s1 == s2: {s1 is s2}')


def class_singleton():
    print('class singleton infos')
    s3 = SingletonClass(3)
    s4 = SingletonClass(4)
    s3.show_id('s3')
    s4.show_id('s4')
    print(f'is s3 == s4: {s3 is s4}')


def decorator_singleton():
    print('decorator singleton infos')
    s5 = SingletonDecorator(5)
    s6 = SingletonDecorator(6)
    s5.show_id('s5')
    s6.show_id('s6')
    print(f'is s5 == s6: {s5 is s6}')


if __name__ == "__main__":
    metaclass_singleton()
    print('*' * 25)
    class_singleton()
    print('*' * 25)
    decorator_singleton()
