from abc import ABC, abstractmethod


# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Concrete Command
class ConcreteCommand(Command):
    def __init__(self, receiver, data):
        self.receiver = receiver
        self.data = data

    def execute(self):
        self.receiver.action(self.data)


# Receiver
class Receiver:

    @staticmethod
    def action(data):
        print(f"Receiver: Performing the action for {data}")


# Invoker
class Invoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        if self.command:
            self.command.execute()


# Client code
def main():
    receiver = Receiver()

    command = ConcreteCommand(receiver, "command_data")

    invoker = Invoker()
    invoker.set_command(command)

    invoker.execute_command()


if __name__ == "__main__":
    main()
