from abc import ABC, abstractmethod
import copy


# Prototype Interface
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


# Concrete Prototype
class Employee(Prototype):
    def __init__(self, name, age, position, salary, department="IT"):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.department = department

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: ${self.salary}, Department: {self.department}"


# Cache
class EmployeeCache:
    def __init__(self):
        self._cache = {}

    def add_prototype(self, key, prototype):
        self._cache[key] = prototype

    def get_prototype(self, key):
        prototype = self._cache.get(key)
        if not prototype:
            raise ValueError(f"Prototype with key '{key}' not found in cache.")
        return prototype.clone()


# Client
def client_code():
    # create prototypes
    developer_prototype = Employee("Unknown", 25, "Software Developer", 70000)
    manager_prototype = Employee("Unknown", 40, "Manager", 90000)
    ceo_prototype = Employee("Unknown", 50, "CEO", 150000)

    # save prototypes in cache
    employee_cache = EmployeeCache()
    employee_cache.add_prototype("developer", developer_prototype)
    employee_cache.add_prototype("manager", manager_prototype)
    employee_cache.add_prototype("ceo", ceo_prototype)

    # create a new employee from the cache
    # get_prototype returns a deep copy of the prototype

    dev1 = employee_cache.get_prototype("developer")
    dev1.name = "Alice"
    dev1.salary = 75000

    dev2 = employee_cache.get_prototype("developer")
    dev2.name = "Bob"
    dev2.department = "R&D"

    manager1 = employee_cache.get_prototype("manager")
    manager1.name = "Charlie"
    manager1.age = 42

    print(dev1)
    print(dev2)
    print(manager1)


def main():
    client_code()


if __name__ == "__main__":
    main()
