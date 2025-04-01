from abc import ABC, abstractmethod


# Abstract Handler
class PaymentHandler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        if self.can_handle(request):
            if self.process(request):
                if self.next_handler:
                    return self.next_handler.handle(request)
                return "Payment succeeded."
        return "Payment failed."

    @abstractmethod
    def can_handle(self, request):
        pass

    @abstractmethod
    def process(self, request):
        pass


# Concrete Handler 1: Authentication Check
class AuthenticationHandler(PaymentHandler):
    def can_handle(self, request):
        return "authenticated" in request

    def process(self, request):
        if request["authenticated"]:
            print("Authentication succeeded.")
            return True
        print("Authentication failed.")
        return False


# Concrete Handler 2: Account Balance Check
class BalanceHandler(PaymentHandler):
    def can_handle(self, request):
        return "amount" in request and "balance" in request

    def process(self, request):
        if request["balance"] >= request["amount"]:
            print(f"Balance check passed: Account balance = {request['balance']}")
            return True
        print(f"Balance check failed: Account balance = {request['balance']}, Required = {request['amount']}")
        return False


# Concrete Handler 3: Daily Limit Check
class DailyLimitHandler(PaymentHandler):
    def can_handle(self, request):
        return "amount" in request and "daily_limit" in request

    def process(self, request):
        if request["amount"] <= request["daily_limit"]:
            print(f"Daily limit check passed: Amount = {request['amount']}, Limit = {request['daily_limit']}")
            return True
        print(f"Daily limit check failed: Amount = {request['amount']}, Limit = {request['daily_limit']}")
        return False


# Chain Builder
class PaymentChainConfigurator:
    @staticmethod
    def get_payment_chain():
        return AuthenticationHandler(
            BalanceHandler(
                DailyLimitHandler()
            )
        )


# Client Code
def main():
    payment_chain = PaymentChainConfigurator.get_payment_chain()

    # Example requests
    requests_list = [
        {
            "authenticated": True,
            "balance": 5000,
            "amount": 1500,
            "daily_limit": 2000
        },
        {
            "authenticated": True,
            "balance": 1000,
            "amount": 1500,
            "daily_limit": 2000
        },
        {
            "authenticated": False,
            "balance": 5000,
            "amount": 1500,
            "daily_limit": 2000
        },
        {
            "authenticated": True,
            "balance": 5000,
            "amount": 2500,
            "daily_limit": 2000
        }
    ]
    for i, request in enumerate(requests_list, 1):
        print(f"Request #{i}")
        print(f"Request: {request}")
        print(f"Response: {payment_chain.handle(request)}")
        print()


if __name__ == "__main__":
    main()
