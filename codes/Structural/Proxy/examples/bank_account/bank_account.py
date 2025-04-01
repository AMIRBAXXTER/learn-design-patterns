from abc import ABC, abstractmethod


# Subject interface
class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


# Concrete subject
class RealBankAccount(BankAccount):
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        print(f"RealBankAccount: Deposited {amount}. Current balance: {self._balance}")

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"RealBankAccount: Withdrawn {amount}. Current balance: {self._balance}")
        else:
            print(f"RealBankAccount: Insufficient funds. Current balance: {self._balance}")


# Proxy -> Protection Proxy
class ProxyBankAccount(BankAccount):
    def __init__(self, real_account, username):
        self._real_account = real_account
        self._authenticated_user = username
        self._authorized_users = {"admin", "user"}

    def _is_authenticated(self):
        if self._authenticated_user in self._authorized_users:
            print(f"ProxyBankAccount: User '{self._authenticated_user}' authenticated successfully.")
            return True
        else:
            print(f"ProxyBankAccount: Access denied for user '{self._authenticated_user}'.")
            return False

    def deposit(self, amount):

        if self._is_authenticated():
            self._real_account.deposit(amount)

    def withdraw(self, amount):

        if self._is_authenticated():
            self._real_account.withdraw(amount)


# Client code
def main():
    real_account = RealBankAccount(balance=500)

    print("\n--- Access with authenticated user ---")
    proxy_account_user = ProxyBankAccount(real_account, "user")
    proxy_account_user.deposit(200)
    proxy_account_user.withdraw(100)
    proxy_account_user.withdraw(1000)

    print("\n--- Access with non-authenticated user ---")
    proxy_account_guest = ProxyBankAccount(real_account, "guest")
    proxy_account_guest.deposit(100)
    proxy_account_guest.withdraw(50)


if __name__ == "__main__":
    main()
