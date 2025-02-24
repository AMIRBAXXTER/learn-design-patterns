from concept import SingletonMeta
import json


class DatabaseConnection(metaclass=SingletonMeta):
    """
    why use singleton design pattern in database connection?

    because we need to connect to database only once, and then we can use it in all of our classes.
    """

    def __init__(self):
        # initialize the connection

        self.connection = 'database connected'


# using the singleton to create an instance

db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1.connection)
print(db1 is db2)


class ConfigManager(metaclass=SingletonMeta):
    """
    why use singleton design pattern in config manager?

    because we need to load config only once, and then we can use it in all of our classes.
    loading config is a heavy operation, so we don't want to do it more than once.
    """

    def __init__(self):
        self.config = self.load_config()

    @staticmethod
    def load_config():
        with open('config.json', 'r') as config_file:
            return json.load(config_file)


config1 = ConfigManager()
config2 = ConfigManager()

print(config1.config)
print(config1 is config2)
