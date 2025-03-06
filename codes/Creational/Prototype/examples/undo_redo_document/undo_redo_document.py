import copy
import time
from abc import ABC, abstractmethod


# Prototype Class: Document
class Document(ABC):
    def __init__(self, content=""):
        self.content = content
        self.history = []  # Stack to store document states for undo/redo
        self.future = []  # Stack to store document states for redo

    @abstractmethod
    def clone(self):
        pass

    def write(self, text):
        # Save current state to history before modifying
        self.history.append(self.clone())
        self.content += text
        self.future = []  # Clear redo history after writing new text
        time.sleep(0.1)  # Simulate writing time

    def undo(self):
        if self.history:
            # Save the current state to the future for potential redo
            self.future.append(self.clone())
            self.content = self.history.pop().content
            print("Undoing...")
            time.sleep(0.05)  # Simulate undo time
        else:
            print("Nothing to undo.")

    def redo(self):
        if self.future:
            # Save the current state to the history for potential undo
            self.history.append(self.clone())
            self.content = self.future.pop().content
            print("Redoing...")
            time.sleep(0.05)  # Simulate redo time
        else:
            print("Nothing to redo.")

    def display(self):
        print("Current Content:\n", self.content)


# Concrete Prototype: TextDocument
class TextDocument(Document):
    def clone(self):
        # Deep copy to create a new instance with independent state
        return copy.deepcopy(self)


# Client Code
if __name__ == "__main__":
    # Create an initial document prototype
    doc = TextDocument()
    print("Starting with a blank document.")
    doc.display()

    # Perform some write operations, saving state
    doc.write("First sentence. ")
    doc.display()

    doc.write("Second sentence. ")
    doc.display()

    doc.write("Third sentence. ")
    doc.display()

    # Undo the last write
    doc.undo()
    doc.display()

    # Redo the last undo
    doc.redo()
    doc.display()

    doc.undo()
    doc.display()

    doc.undo()
    doc.display()

    # Redo twice
    doc.redo()
    doc.display()

    doc.redo()
    doc.display()

    doc.redo()  # Nothing to redo
