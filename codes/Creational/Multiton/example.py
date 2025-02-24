import logging


class Logger:
    """
    why use multiton design pattern in logger?

    because we need to create a logger for each file, and then we can use it in all of our classes.
    creating a logger is a heavy operation, so we don't want to do it more than once for each file.
    """
    _instance = {}

    def __new__(cls, log_file="app.log", *args, **kwargs):
        """
        check if the logger is already created for this file class_name, if not create it
        """
        if log_file not in cls._instance:
            cls._instance[log_file] = super().__new__(cls)
        return cls._instance[log_file]

    def __init__(self, log_file="app.log"):
        if not hasattr(self, 'logger'):
            self.logger = logging.getLogger(log_file)
            self.logger.setLevel(logging.DEBUG)  # تنظیم سطح لاگ
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def error(self, message):
        self.logger.error(message)


class UserContext:
    _instances = {}

    def __new__(cls, user_id, *args, **kwargs):
        if user_id not in cls._instances:
            cls._instances[user_id] = super(UserContext, cls).__new__(cls)
        return cls._instances[user_id]

    def __init__(self, user_id):
        self.user_id = user_id
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)


logger1 = Logger()
logger2 = Logger()
logger3 = Logger(log_file="test.log")

logger1.info("This is an INFO message.")
logger1.debug("This is a DEBUG message.")
logger2.error("This is an ERROR message.")
logger3.info("This is an INFO message in test.log.")

print(logger1 is logger2)
print(logger1 is logger3)

user1_context = UserContext(1)
user2_context = UserContext(2)
user1_context_duplicate = UserContext(1)

user1_context.set("language", "fa")
user2_context.set("language", "en")

print(user1_context.get("language"))
print(user2_context.get("language"))
print(user1_context is user1_context_duplicate)
