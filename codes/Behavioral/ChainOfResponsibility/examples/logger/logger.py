import os
import sqlite3
from abc import ABC, abstractmethod


# Abstract Handler
class Logger(ABC):
    def __init__(self, next_logger=None):
        self.next_logger = next_logger

    def log(self, message, level):
        if self.can_handle(level):
            self.write_log(message)
        elif self.next_logger:
            self.next_logger.log(message, level)
        else:
            print(f"No logger found for level: {level}")

    @abstractmethod
    def can_handle(self, level):
        pass

    @abstractmethod
    def write_log(self, message):
        pass


# Console Logger (ConcreteHandler1)
class ConsoleLogger(Logger):
    def can_handle(self, level):
        return level == "console"

    def write_log(self, message):
        print(f"Console log: {message}")


# File Logger (ConcreteHandler2)
class FileLogger(Logger):
    def __init__(self, next_logger=None, file_path="logfile.txt"):
        super().__init__(next_logger)
        self.file_path = file_path

    def can_handle(self, level):
        return level == "file"

    def write_log(self, message):
        with open(self.file_path, "a") as file:
            file.write(f"File log: {message}\n")


# Database Logger (ConcreteHandler3)
class DatabaseLogger(Logger):
    def __init__(self, next_logger=None, db_path="logs.db"):
        super().__init__(next_logger)
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        if not os.path.exists(self.db_path):
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(
                "CREATE TABLE logs (id INTEGER PRIMARY KEY, message TEXT)"
            )
            conn.commit()
            conn.close()

    def can_handle(self, level):
        return level == "db"

    def write_log(self, message):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO logs (message) VALUES (?)", (message,))
        conn.commit()
        conn.close()


# Chain Builder
class LoggerChainConfigurator:
    @staticmethod
    def get_logger_chain():
        return ConsoleLogger(
            FileLogger(
                DatabaseLogger()
            )
        )


# Client code
def main():
    logger_chain = LoggerChainConfigurator.get_logger_chain()

    # Example messages
    logger_chain.log("This is a console message.", "console")
    logger_chain.log("This is a file message.", "file")
    logger_chain.log("This is a database message.", "db")
    logger_chain.log("This is an unknown message.", "unknown")


if __name__ == "__main__":
    main()
