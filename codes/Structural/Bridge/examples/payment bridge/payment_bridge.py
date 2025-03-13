from abc import ABC, abstractmethod


# Abstract Implementor
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Implementors
class PayPalPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid {amount} USD using PayPal.")


class CreditCardPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid {amount} USD using Credit Card.")


# Abstraction
class Purchase(ABC):

    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    @abstractmethod
    def make_purchase(self, amount):
        pass


# Concrete Abstractions
class ProductPurchase(Purchase):

    def make_purchase(self, amount):
        print("Processing product purchase...")
        self.payment_method.pay(amount)


class ServicePurchase(Purchase):

    def make_purchase(self, amount):
        print("Processing service purchase...")
        self.payment_method.pay(amount)


# Client Code
def main():

    paypal = PayPalPayment()

    product_purchase = ProductPurchase(paypal)
    product_purchase.make_purchase(50)

    print("\n")

    credit_card = CreditCardPayment()

    service_purchase = ServicePurchase(credit_card)
    service_purchase.make_purchase(100)

    print("\n")

    another_product_purchase = ProductPurchase(credit_card)
    another_product_purchase.make_purchase(75)


if __name__ == "__main__":
    main()
