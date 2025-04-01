import os


# Command Interface
class Command:
    def execute(self):
        pass

    def undo(self):
        pass


# Concrete Command: Create File
class CreateFileCommand(Command):
    def __init__(self, filename, content=""):
        self.filename = filename
        self.content = content

    def execute(self):
        with open(self.filename, "w") as file:
            file.write(self.content)
        print(f"File '{self.filename}' created.")

    def undo(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"File '{self.filename}' deleted (Undo).")
        else:
            print(f"File '{self.filename}' does not exist for Undo.")


# Concrete Command: Delete File
class DeleteFileCommand(Command):
    def __init__(self, filename):
        self.filename = filename
        self.backup_content = None

    def execute(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.backup_content = file.read()
            os.remove(self.filename)
            print(f"File '{self.filename}' deleted.")
        else:
            print(f"File '{self.filename}' does not exist.")

    def undo(self):
        if self.backup_content:
            with open(self.filename, "w") as file:
                file.write(self.backup_content)
            print(f"Undo delete: File '{self.filename}' restored.")
        else:
            print(f"Cannot undo delete for file '{self.filename}' as no backup is available.")


# Concrete Command: Rename File
class RenameFileCommand(Command):
    def __init__(self, old_filename, new_filename):
        self.old_filename = old_filename
        self.new_filename = new_filename

    def execute(self):
        if os.path.exists(self.old_filename):
            os.rename(self.old_filename, self.new_filename)
            print(f"File '{self.old_filename}' renamed to '{self.new_filename}'.")
        else:
            print(f"File '{self.old_filename}' does not exist.")

    def undo(self):
        if os.path.exists(self.new_filename):
            os.rename(self.new_filename, self.old_filename)
            print(f"Undo rename: File '{self.new_filename}' renamed back to '{self.old_filename}'.")
        else:
            print(f"File '{self.new_filename}' does not exist for Undo.")


# Invoker: FileManager
class FileManager:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        if self.history:
            command = self.history.pop()
            command.undo()
        else:
            print("No commands to undo.")


# Client Code
def main():
    file_manager = FileManager()

    # Example commands
    create_command = CreateFileCommand("example.txt", "Hello, World!")
    delete_command = DeleteFileCommand("example_renamed.txt")
    rename_command = RenameFileCommand("example.txt", "example_renamed.txt")

    # Execute commands
    print("\nExecuting Create Command:")
    file_manager.execute_command(create_command)

    print("\nExecuting Rename Command:")
    file_manager.execute_command(rename_command)

    print("\nExecuting Create Command Again:")
    file_manager.execute_command(create_command)

    print("\nExecuting Delete Command:")
    file_manager.execute_command(delete_command)

    print("\nUndo Delete Command:")
    file_manager.undo_last()


if __name__ == "__main__":
    main()
