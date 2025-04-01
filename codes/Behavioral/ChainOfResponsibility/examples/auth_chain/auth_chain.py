from abc import ABC, abstractmethod


# Handler interface
class AuthenticationHandler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        if self.can_handle(request):
            self.process(request)
        elif self.next_handler:
            self.next_handler.handle(request)
        else:
            print("Authentication failed.")

    @abstractmethod
    def can_handle(self, request):
        pass

    @abstractmethod
    def process(self, request):
        pass


# ConcreteHandler1: Password authentication
class PasswordHandler(AuthenticationHandler):
    def can_handle(self, request):
        return "password" in request

    def process(self, request):
        if request["password"] == "secure123":
            print("Authentication successful.")
        else:
            print("Invalid password.")


# ConcreteHandler2: Two-factor authentication
class TwoFactorHandler(AuthenticationHandler):
    def can_handle(self, request):
        return "otp" in request

    def process(self, request):
        if request["otp"] == "123456":
            print("Authentication successful.")
        else:
            print("Invalid OTP.")


# ConcreteHandler3: Role-based access check
class RoleHandler(AuthenticationHandler):
    def can_handle(self, request):
        return "role" in request

    def process(self, request):
        if request["role"] == "admin":
            print("Authentication successful.")
        else:
            print("Access denied.")


# Chain Builder
class AuthenticationConfigurator:
    def __init__(self):
        self._auth_chain = self.get_auth_chain()

    @staticmethod
    def get_auth_chain():
        return PasswordHandler(
            TwoFactorHandler(
                RoleHandler()
            )
        )

    def authenticate(self, request):
        self._auth_chain.handle(request)


# Client code
def main():
    auth_chain = AuthenticationConfigurator()

    requests = [
        {"password": "secure123"},
        {"password": "insecure123"},
        {"otp": "123456"},
        {"otp": "654321"},
        {"role": "admin"},
        {"role": "user"},
    ]

    for request in requests:
        auth_chain.authenticate(request)
        print("-" * 10)


if __name__ == "__main__":
    main()
