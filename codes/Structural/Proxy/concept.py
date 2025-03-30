from abc import ABC, abstractmethod


# Subject interface
class Subject(ABC):
    @abstractmethod
    def perform_action(self):
        pass


# Concrete subject
class RealSubject(Subject):
    def perform_action(self):
        print("RealSubject: Performing the action.")


# Proxy
class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def perform_action(self):
        print("Proxy: Perform proxy action before calling real subject")
        self._real_subject.perform_action()


# Client code
def main():
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    print("Client: Calling the Proxy to perform the action.")
    proxy.perform_action()


if __name__ == "__main__":
    main()
