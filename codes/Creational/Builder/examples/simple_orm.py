from abc import ABC, abstractmethod


# Product: SQL Query
class SQLQuery:
    def __init__(self):
        self.select = []
        self.from_table = None
        self.where = []
        self.group_by = []
        self.order_by = []
        self.limit = None

    def __str__(self):
        query = "SELECT " + ", ".join(self.select) + " FROM " + self.from_table
        if self.where:
            query += " WHERE " + " AND ".join(self.where)
        if self.group_by:
            query += " GROUP BY " + ", ".join(self.group_by)
        if self.order_by:
            query += " ORDER BY " + ", ".join(self.order_by)
        if self.limit:
            query += " LIMIT " + str(self.limit)
        return query


# Abstract Builder
class SQLQueryBuilder(ABC):
    def __init__(self):
        self.query = SQLQuery()

    @abstractmethod
    def select(self, columns):
        pass

    @abstractmethod
    def from_table(self, table_name):
        pass

    @abstractmethod
    def where(self, condition):
        pass

    @abstractmethod
    def group_by(self, columns):
        pass

    @abstractmethod
    def order_by(self, columns):
        pass

    @abstractmethod
    def limit(self, max_rows):
        pass

    def get_query(self):
        return self.query


# Concrete Builder
class UserSQLQueryBuilder(SQLQueryBuilder):
    def select(self, columns):
        self.query.select.extend(columns)
        return self

    def from_table(self, table_name):
        self.query.from_table = table_name
        return self

    def where(self, condition):
        self.query.where.append(condition)
        return self

    def group_by(self, columns):
        self.query.group_by.extend(columns)
        return self

    def order_by(self, columns):
        self.query.order_by.extend(columns)
        return self

    def limit(self, max_rows):
        self.query.limit = max_rows
        return self


# Director (Optional, can be used to construct specific queries)
class SQLQueryDirector:
    def __init__(self, builder: SQLQueryBuilder):
        self.builder = builder

    def construct_user_query(self, columns, table_name, conditions, group_by, order_by, limit):
        self.builder.select(columns).from_table(table_name)
        for condition in conditions:
            self.builder.where(condition)
        if group_by:
            self.builder.group_by(group_by)
        if order_by:
            self.builder.order_by(order_by)
        if limit:
            self.builder.limit(limit)


# Client Code
def client_code():
    builder = UserSQLQueryBuilder()
    director = SQLQueryDirector(builder)

    columns = ["id", "username", "email"]
    table_name = "users"
    conditions = ["age > 18", "is_active = True"]
    group_by = ["city"]
    order_by = ["username"]
    limit = 10

    director.construct_user_query(columns, table_name, conditions, group_by, order_by, limit)
    query = builder.get_query()

    print(query)


if __name__ == "__main__":
    client_code()
