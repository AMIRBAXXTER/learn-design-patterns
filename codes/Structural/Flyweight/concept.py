from typing import Dict
from abc import ABC, abstractmethod


# Flyweight Interface
class Flyweight(ABC):

    @abstractmethod
    def operation(self, extrinsic_state: str) -> None:
        pass


# Concrete Flyweight
class ConcreteFlyweight(Flyweight):

    def __init__(self, intrinsic_state: str) -> None:
        self.intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state: str) -> None:
        print(f"Intrinsic State: {self.intrinsic_state}, Extrinsic State: {extrinsic_state}")


# Flyweight Factory
class FlyweightFactory:
    def __init__(self) -> None:
        self._flyweights: Dict[str, Flyweight] = {}

    def get_flyweight(self, key: str) -> Flyweight:
        if key not in self._flyweights:
            print(f"Creating new Flyweight for key: {key}")
            self._flyweights[key] = ConcreteFlyweight(key)
        else:
            print(f"Reusing existing Flyweight for key: {key}")
        return self._flyweights[key]

    def list_flyweights(self) -> None:
        print(f"Flyweights in Factory: {list(self._flyweights.keys())}")


# Client Code
def main():
    factory = FlyweightFactory()

    flyweight_a = factory.get_flyweight("state_A")
    flyweight_b = factory.get_flyweight("state_B")
    flyweight_a2 = factory.get_flyweight("state_A")

    flyweight_a.operation("unique1")
    flyweight_b.operation("unique2")
    flyweight_a2.operation("unique3")

    factory.list_flyweights()


if __name__ == "__main__":
    main()
