import os
from abc import ABC, abstractmethod

import blessings

terminal = blessings.Terminal(force_styling=True)


# Flyweight Interface
class LogType(ABC):
    @abstractmethod
    def display(self, message: str) -> None:
        pass


# Concrete Flyweight
class ColoredLogType(LogType):
    def __init__(self, color_function, color_name: str):
        self.color_function = color_function
        self.color_name = color_name

    def display(self, message: str) -> None:
        # remove (B in pycharm terminal
        result = f"{terminal.bold}[{self.color_name}] {self.color_function(message)}"
        print(result.replace("(B", "") if "PYCHARM_HOSTED" in os.environ else result)


# Flyweight Factory
class LogTypeFactory:
    _log_types = {}

    @classmethod
    def get_log_type(cls, color_name: str) -> LogType or None:
        if color_name not in cls._log_types:
            color_function = cls._get_color_function(color_name)
            if color_function is not None:
                print(f"creating new LogType with color: {color_name}")
                cls._log_types[color_name] = ColoredLogType(color_function, color_name)
            else:
                print(f"invalid color name: {color_name}")
                return None
        else:
            print(f"reusing existing LogType with color: {color_name}")
        return cls._log_types[color_name]

    @classmethod
    def _get_color_function(cls, color_name: str):
        if color_name.lower() in blessings.COLORS:
            return getattr(terminal, color_name.lower(), None)
        return None

    @classmethod
    def log_type_count(cls) -> int:
        return len(cls._log_types)


# Context
class LogContext:
    def __init__(self, color_name: str, message: str):
        self.log_type = LogTypeFactory.get_log_type(color_name)
        self.message = message

    def show_log(self) -> None:
        if self.log_type:
            self.log_type.display(self.message)


# Client code
def main():
    logs = [
        ("red", "This is an Error log."),
        ("yellow", "This is a Warning log."),
        ("blue", "This is an Info log."),
        ("green", "This is an Success log."),
        ("grey", "This is an Invalid log."),
        ("red", "This is another Error log."),
    ]
    for color, msg in logs:
        log = LogContext(color, msg)
        log.show_log()

    print(f"\nTotal LogTypes created: {LogTypeFactory.log_type_count()}")


if __name__ == "__main__":
    main()
