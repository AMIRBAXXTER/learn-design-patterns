from abc import ABC, abstractmethod
import copy


# Prototype Interface
class BasePrototype(ABC):
    @abstractmethod
    def clone(self):
        pass


# Concrete Prototype
class ConcretePrototype(BasePrototype):
    def __init__(self, data, mutable_data):
        self.data = data
        self.mutable_data = mutable_data

    def clone(self, deepcopy=False):
        return copy.deepcopy(self) if deepcopy else copy.copy(self)

    def __str__(self):
        return f"Data: {self.data}, Mutable Data: {self.mutable_data}"


# Client
def client_code():
    # Create a prototype
    prototype = ConcretePrototype(
        data="Initial Data",
        mutable_data=[1, 2, 3]
    )

    # Clone the prototype (shallow copy)
    clone1 = prototype.clone()
    print("Clone 1 (Shallow):", clone1)

    # Modify mutable data in the clone
    clone1.mutable_data.append(4)
    print("Clone 1 (Shallow) After Modification:", clone1)
    print("Prototype After Clone 1 Modification:", prototype)  # Prototype is also changed

    # Clone the prototype (deep copy)
    clone2 = prototype.clone(deepcopy=True)
    print("Clone 2 (Deep):", clone2)

    # Modify mutable data in the deep copy clone
    clone2.mutable_data.append(5)
    print("Clone 2 (Deep) After Modification:", clone2)
    print("Prototype After Clone 2 Modification:", prototype)  # Prototype remains unchanged


if __name__ == "__main__":
    client_code()
