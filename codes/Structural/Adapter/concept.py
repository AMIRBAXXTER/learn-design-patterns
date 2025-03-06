# Target Interface
class Target:
    def request(self):
        return "Target: The default target's behavior."


# Adaptee Class
class Adaptee:

    @staticmethod
    def specific_request():
        return ".eetpadA eht fo roivaheb laicepS"  # A specific, incompatible request


# Adapter Class
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


# Client Code
def client_code(target: Target):
    print(target.request())


def main():
    default_target = Target()
    client_code(default_target)

    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    client_code(adapter)


if __name__ == "__main__":
    main()
