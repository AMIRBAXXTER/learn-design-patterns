from abc import ABC, abstractmethod


class Discount(ABC):

    @abstractmethod
    def calculate(self, price):
        pass


class RegularDiscount(Discount):

    def calculate(self, price):
        return price * 1


class LoyalDiscount(Discount):

    def calculate(self, price):
        return price * 0.9


class VipDiscount(Discount):

    def calculate(self, price):
        return price * 0.8


class DiscountFactory:

    @staticmethod
    def create_discount(discount_type):
        cases = {
            'regular': RegularDiscount,
            'loyal': LoyalDiscount,
            'vip': VipDiscount
        }
        if discount_type in cases:
            return cases[discount_type]()
        else:
            raise ValueError(f'{discount_type} is not a valid discount type')


def main():
    regular_discount = DiscountFactory.create_discount('regular')
    print(regular_discount.calculate(100))
    loyal_discount = DiscountFactory.create_discount('loyal')
    print(loyal_discount.calculate(100))
    vip_discount = DiscountFactory.create_discount('vip')
    print(vip_discount.calculate(100))
    try:
        invalid_discount = DiscountFactory.create_discount('nice')
        print(invalid_discount.calculate(100))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
