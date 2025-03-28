# Subsystem A
class SubsystemA:
    def operation_a(self):
        return f"SubsystemA: Operation A executed {self}."


# Subsystem B
class SubsystemB:
    def operation_b(self):
        return f"SubsystemB: Operation B executed {self}."


# Subsystem C
class SubsystemC:
    def operation_c(self):
        return f"SubsystemC: Operation C executed {self}."


# Facade
class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()
        self._subsystem_c = SubsystemC()

    def operation(self):
        result_a = self._subsystem_a.operation_a()
        result_b = self._subsystem_b.operation_b()
        result_c = self._subsystem_c.operation_c()
        return f"Facade combines:\n{result_a}\n{result_b}\n{result_c}"


# Client code
def main():
    facade = Facade()
    print(facade.operation())


if __name__ == "__main__":
    main()
