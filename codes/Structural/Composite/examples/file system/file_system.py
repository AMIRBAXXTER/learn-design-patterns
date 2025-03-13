from abc import ABC, abstractmethod


# Component
class FileSystemItem(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def display(self, indent=2):
        pass

    def add(self, item: "FileSystemItem"):
        print(f"Cannot add {item.name} to {self.__class__.__name__}")

    def remove(self, item: "FileSystemItem"):
        print(f"Cannot remove {item.name} from {self.__class__.__name__}")


# Leaf -> a simple component
class File(FileSystemItem):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def get_size(self):
        return self.size

    def display(self, indent=0):
        print(" " * indent + f"File: {self.name} ({self.size} bytes)")


# Composite -> a complex component that can have children
class Folder(FileSystemItem):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, item: FileSystemItem):
        self.children.append(item)

    def remove(self, item: FileSystemItem):
        self.children.remove(item)

    def get_size(self):
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size

    def display(self, indent=2):
        print(" " * indent + f"Folder: {self.name}")
        for child in self.children:
            child.display(indent + 2)


# Client Code
def main():
    file1 = File("Document1.txt", 1200)
    file2 = File("Image1.jpg", 5600)
    file3 = File("Music1.mp3", 3400000)
    file1.add(file2)

    folder1 = Folder("Documents")
    folder1.add(file1)
    folder1.add(file2)

    root_folder = Folder("Root")
    root_folder.add(folder1)
    root_folder.add(file3)

    print("File System Structure:")
    root_folder.display()

    print("\nTotal Size of Files:")
    print(f"{root_folder.get_size()} bytes")


if __name__ == "__main__":
    main()
