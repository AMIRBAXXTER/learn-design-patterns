from typing import Dict
from abc import ABC, abstractmethod


# Flyweight Interface
class TreeTypeInterface(ABC):
    @abstractmethod
    def render(self, x: int, y: int):
        pass


# Concrete Flyweight
class TreeType(TreeTypeInterface):
    def __init__(self, tree_type: str, color: str, texture: str) -> None:
        self.tree_type = tree_type
        self.color = color
        self.texture = texture

    def render(self, x: int, y: int):
        print(
            f"Rendering tree of type {self.tree_type} "
            f"at ({x}, {y}) with color {self.color} and texture {self.texture}"
        )


# Flyweight Factory
class TreeFactory:
    _tree_types: Dict[str, TreeType] = {}

    @classmethod
    def get_tree_type(cls, tree_type: str, color: str, texture: str) -> TreeType:
        key = f"{tree_type}_{color}_{texture}"
        if key not in cls._tree_types:
            print(f"Creating new TreeType for key: {key}")
            cls._tree_types[key] = TreeType(tree_type, color, texture)
        else:
            print(f"Reusing existing TreeType for key: {key}")
        return cls._tree_types[key]

    @classmethod
    def list_tree_types(cls) -> None:
        print(f"TreeTypes in Factory: {list(cls._tree_types.keys())}")


# Context
class Tree:
    def __init__(self, position: tuple[int, int], tree_type: TreeTypeInterface) -> None:
        self.position = position
        self.tree_type = tree_type

    def render(self):
        self.tree_type.render(*self.position)


# Client Code
class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, position: tuple[int, int], tree_type_obj: TreeTypeInterface):
        tree = Tree(position, tree_type_obj)
        self.trees.append(tree)

    def render(self):
        for tree in self.trees:
            tree.render()


def main():
    forest = Forest()

    oak_tree = TreeFactory.get_tree_type("Oak", "Green", "Rough")
    pine_tree = TreeFactory.get_tree_type("Pine", "Dark Green", "Smooth")
    oak_tree2 = TreeFactory.get_tree_type("Oak", "Green", "Rough")

    forest.plant_tree((1, 1), oak_tree)
    forest.plant_tree((2, 2), pine_tree)
    forest.plant_tree((3, 3), oak_tree2)
    forest.plant_tree((4, 4), pine_tree)

    forest.render()

    TreeFactory.list_tree_types()


if __name__ == "__main__":
    main()
