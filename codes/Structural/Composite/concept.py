from abc import ABC, abstractmethod


# Component
class BaseComponent(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def operation(self):
        pass

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def is_composite(self):
        return False


# Leaf -> a simple component
class LeafClass(BaseComponent):

    def operation(self):
        return f"Leaf {self.name}"


# Composite -> a complex component that can have children
class CompositeClass(BaseComponent):

    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        results = []
        for child in self.children:
            results.append(child.operation())
        return f"Composite {self.name}: ({', '.join(results)})"

    def is_composite(self):
        return True


# Client
def client_code(component1: BaseComponent, component2: BaseComponent = None):
    if component2:
        if component1.is_composite():
            component1.add(component2)
    print(f"RESULT: {component1.operation()}", end="")


# Usage
if __name__ == "__main__":
    leaf_1 = LeafClass("1")
    leaf_2 = LeafClass("2")

    print("Client: I get a simple component:")
    client_code(leaf_1)
    print("\n")

    tree = CompositeClass("Tree")
    branch1 = CompositeClass("Branch1")
    branch1.add(leaf_1)
    branch1.add(leaf_2)
    tree.add(branch1)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:\n")
    client_code(tree, leaf_1)
    print("\n")
