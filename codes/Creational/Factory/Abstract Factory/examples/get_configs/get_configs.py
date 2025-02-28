from abc import ABC, abstractmethod


# Abstract Factory
class ConfigFactory(ABC):
    @abstractmethod
    def create_database_config(self):
        pass

    @abstractmethod
    def create_service_config(self):
        pass

    @abstractmethod
    def create_app_config(self):
        pass


# Concrete Factory for development configs
class DevConfigFactory(ConfigFactory):
    def create_database_config(self):
        return DevDatabaseConfig()

    def create_service_config(self):
        return DevServiceConfig()

    def create_app_config(self):
        return DevAppConfig()


# Concrete Factory for testing configs
class TestConfigFactory(ConfigFactory):
    def create_database_config(self):
        return TestDatabaseConfig()

    def create_service_config(self):
        return TestServiceConfig()

    def create_app_config(self):
        return TestAppConfig()


# Concrete Factory for production configs
class ProdConfigFactory(ConfigFactory):
    def create_database_config(self):
        return ProdDatabaseConfig()

    def create_service_config(self):
        return ProdServiceConfig()

    def create_app_config(self):
        return ProdAppConfig()


# Abstract Products for Database configs
class DatabaseConfig(ABC):
    @abstractmethod
    def get_connection_string(self):
        pass


# Abstract Products for Service configs
class ServiceConfig(ABC):
    @abstractmethod
    def get_service_url(self):
        pass


# Abstract Products for App configs
class AppConfig(ABC):
    @abstractmethod
    def get_app_name(self):
        pass


# Concrete Products for Development Database configs
class DevDatabaseConfig(DatabaseConfig):
    def get_connection_string(self):
        return "localhost:5432/dev_db"


# Concrete Products for Development Service configs
class DevServiceConfig(ServiceConfig):
    def get_service_url(self):
        return "http://localhost:8080/dev_service"


# Concrete Products for Development App configs
class DevAppConfig(AppConfig):
    def get_app_name(self):
        return "DevApp"


# Concrete Products for Testing Database configs
class TestDatabaseConfig(DatabaseConfig):
    def get_connection_string(self):
        return "testserver:5432/test_db"


# Concrete Products for Testing Service configs
class TestServiceConfig(ServiceConfig):
    def get_service_url(self):
        return "http://testserver:8080/test_service"


# Concrete Products for Testing App configs
class TestAppConfig(AppConfig):
    def get_app_name(self):
        return "TestApp"


# Concrete Products for Production  Database configs
class ProdDatabaseConfig(DatabaseConfig):
    def get_connection_string(self):
        return "prodserver:5432/prod_db"


# Concrete Products for Production Service configs
class ProdServiceConfig(ServiceConfig):
    def get_service_url(self):
        return "http://prodserver:8080/prod_service"


# Concrete Products for Production App configs
class ProdAppConfig(AppConfig):
    def get_app_name(self):
        return "ProdApp"


# Client Code
def client_code(factory: ConfigFactory):
    database_config = factory.create_database_config()
    service_config = factory.create_service_config()
    app_config = factory.create_app_config()

    print(f"Database Connection String: {database_config.get_connection_string()}")
    print(f"Service URL: {service_config.get_service_url()}")
    print(f"App Name: {app_config.get_app_name()}")


def main():
    print("Development Environment:")
    client_code(DevConfigFactory())

    print("\nTesting Environment:")
    client_code(TestConfigFactory())

    print("\nProduction Environment:")
    client_code(ProdConfigFactory())


if __name__ == "__main__":
    main()
