import copy
import time
from time import sleep


class BasePrototype:

    def __init__(self):
        self.data = None

    def clone(self, deepcopy=False):
        return copy.deepcopy(self) if deepcopy else copy.copy(self)


class DataBaseSimulator(BasePrototype):

    def __init__(self, my_id):
        super().__init__()
        self.data = self.get_data(my_id)

    def clone(self, deepcopy=False):
        if isinstance(self.data, (list, dict, set)):
            deepcopy = True
        return super().clone(deepcopy)

    @staticmethod
    def get_data(my_id):
        sleep(1)
        return f'example data for id: {my_id}'


def client_code():
    start = time.perf_counter()
    prototype = DataBaseSimulator(1)
    print(prototype.data)
    clone = prototype.clone()
    print(clone.data)
    end = time.perf_counter()
    print(f'client code runtimes: {end - start}')


def without_prototype():
    start = time.perf_counter()
    instance1 = DataBaseSimulator(1)
    print(instance1.data)
    instance2 = DataBaseSimulator(1)
    print(instance2.data)
    end = time.perf_counter()
    print(f'without prototype runtimes: {end - start}')


def main():
    client_code()
    without_prototype()


if __name__ == "__main__":
    main()
