from abc import ABC, abstractmethod
from blessings import Terminal

t = Terminal()


# Component
class CompanyMember(ABC):
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def display_structure(self, indent=2):
        pass


# Leaf
class Employee(CompanyMember):
    def get_salary(self):
        return self.salary

    def display_structure(self, indent=2):
        print(t.green(" " * indent + f"{self.position}: {self.name} (Salary: ${self.salary})"))


# Composite
class Manager(CompanyMember):
    def __init__(self, name, position, salary):
        super().__init__(name, position, salary)
        self.subordinates = []

    def add(self, member: CompanyMember):
        self.subordinates.append(member)

    def remove(self, member: CompanyMember):
        self.subordinates.remove(member)

    def get_salary(self):
        return self.salary + sum(subordinate.get_salary() for subordinate in self.subordinates)

    def display_structure(self, indent=2):
        print(f'{" " * indent}{t.red("-")} {t.blue(f"{self.position}: {self.name} (Salary: ${self.salary}")}')
        print(t.yellow(" " * indent + "Subordinates:"))
        for subordinate in self.subordinates:
            subordinate.display_structure(indent + 4)


def main():

    emp1 = Employee("Alice", "Junior Developer", 50000)
    emp2 = Employee("Bob", "Senior Developer", 80000)
    emp3 = Employee("Charlie", "UI/UX Designer", 60000)

    manager1 = Manager("David", "Team Lead", 100000)
    manager1.add(emp1)
    manager1.add(emp2)

    manager2 = Manager("Elena", "Creative Lead", 120000)
    manager2.add(emp3)

    senior_manager = Manager("Frank", "CTO", 200000)
    senior_manager.add(manager1)
    senior_manager.add(manager2)

    print("Company Structure:")
    senior_manager.display_structure()
    
    print("\nTotal Salary Expense:")
    print(f"${senior_manager.get_salary()}")


if __name__ == "__main__":
    main()
