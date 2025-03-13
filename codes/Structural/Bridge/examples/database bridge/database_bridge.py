from abc import ABC, abstractmethod


# Abstract Implementor
class DatabaseConnector(ABC):
    """
    Interface برای اتصال به پایگاه‌های داده (Implementor).
    """

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass

    @abstractmethod
    def close_connection(self):
        pass


# Concrete Implementors
class PostgreSQLConnector(DatabaseConnector):

    def connect(self):
        print("Connecting to PostgreSQL database...")
        # کد واقعی اتصال به PostgreSQL اینجا قرار می‌گیرد
        return "PostgreSQL Connection"  # شبیه‌سازی اتصال

    def execute_query(self, query):
        print(f"Executing query on PostgreSQL: {query}")
        # کد واقعی اجرای کوئری در PostgreSQL اینجا قرار می‌گیرد
        return "PostgreSQL Query Result"  # شبیه‌سازی نتیجه کوئری

    def close_connection(self):
        print("Closing PostgreSQL connection.")
        # کد واقعی بستن اتصال PostgreSQL اینجا قرار می‌گیرد


class MySQLConnector(DatabaseConnector):
    def connect(self):
        print("Connecting to MySQL database...")
        # کد واقعی اتصال به MySQL اینجا قرار می‌گیرد
        return "MySQL Connection"  # شبیه‌سازی اتصال

    def execute_query(self, query):
        print(f"Executing query on MySQL: {query}")
        # کد واقعی اجرای کوئری در MySQL اینجا قرار می‌گیرد
        return "MySQL Query Result"  # شبیه‌سازی نتیجه کوئری

    def close_connection(self):
        print("Closing MySQL connection.")
        # کد واقعی بستن اتصال MySQL اینجا قرار می‌گیرد


class SQLiteConnector(DatabaseConnector):

    def connect(self):
        print("Connecting to SQLite database...")
        # کد واقعی اتصال به SQLite اینجا قرار می‌گیرد
        return "SQLite Connection"  # شبیه‌سازی اتصال

    def execute_query(self, query):
        print(f"Executing query on SQLite: {query}")
        # کد واقعی اجرای کوئری در SQLite اینجا قرار می‌گیرد
        return "SQLite Query Result"  # شبیه‌سازی نتیجه کوئری

    def close_connection(self):
        print("Closing SQLite connection.")
        # کد واقعی بستن اتصال SQLite اینجا قرار می‌گیرد


# Abstraction
class DatabaseService(ABC):
    def __init__(self, connector: DatabaseConnector):
        self.connector = connector
        self.connection = None

    def connect_to_db(self):
        self.connection = self.connector.connect()

    def disconnect_from_db(self):
        if self.connection:
            self.connector.close_connection()
            self.connection = None

    @abstractmethod
    def get_data(self, query):
        pass

    @abstractmethod
    def save_data(self, data):
        pass


# Concrete Abstractions
class UserDataService(DatabaseService):
    """
    سرویس داده برای مدیریت اطلاعات کاربران.
    """

    def get_data(self, query):
        self.connect_to_db()
        result = self.connector.execute_query(query)
        self.disconnect_from_db()
        return f"User Data: {result}"

    def save_data(self, data):
        self.connect_to_db()
        query = f"INSERT INTO users VALUES ({data})"
        result = self.connector.execute_query(query)
        self.disconnect_from_db()
        return f"Save User Result: {result}"


class ProductDataService(DatabaseService):
    """
    سرویس داده برای مدیریت اطلاعات محصولات.
    """

    def get_data(self, query):
        self.connect_to_db()
        result = self.connector.execute_query(query)
        self.disconnect_from_db()
        return f"Product Data: {result}"

    def save_data(self, data):
        self.connect_to_db()
        query = f"INSERT INTO products VALUES ({data})"
        result = self.connector.execute_query(query)
        self.disconnect_from_db()
        return f"Save Product Result: {result}"


# Client Code
def main():
    # * استفاده از PostgreSQL برای سرویس داده کاربر
    postgres_connector = PostgreSQLConnector()
    user_service_postgres = UserDataService(postgres_connector)
    print(user_service_postgres.get_data("SELECT * FROM users"))
    print(user_service_postgres.save_data("('John Doe', 30)"))

    print("\n")

    # * استفاده از MySQL برای سرویس داده محصول
    mysql_connector = MySQLConnector()
    product_service_mysql = ProductDataService(mysql_connector)
    print(product_service_mysql.get_data("SELECT * FROM products"))
    print(product_service_mysql.save_data("('Laptop', 1200)"))

    print("\n")

    # * استفاده از SQLite برای سرویس داده کاربر (به عنوان مثال برای تست یا توسعه محلی)
    sqlite_connector = SQLiteConnector()
    user_service_sqlite = UserDataService(sqlite_connector)
    print(user_service_sqlite.get_data("SELECT * FROM users"))
    print(user_service_sqlite.save_data("('Jane Doe', 25)"))


if __name__ == "__main__":
    main()
