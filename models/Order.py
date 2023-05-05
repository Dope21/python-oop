from typing import List
from enum import Enum

from .Payment import Payment
from .Shipping import Shipping
from .Product import Product


class OrderStatus(Enum):
    OPEN = 0
    CLOSE = 1


class OrderItem:
    def __init__(self, product: Product, qty: int, price: float):
        self.__product = product
        self.__qty = qty
        self.__price = price

    @property
    def product(self):
        return self.__product

    @property
    def qty(self):
        return self.__qty

    @property
    def price(self):
        return self.__price


class Order:
    def __init__(
        self,
        email: str,
        items: List[OrderItem],
        shipping: Shipping,
        payment: Payment,
        status: OrderStatus,
        code: str,
    ):
        self.__email = email
        self.__items = items
        self.__shipping = shipping
        self.__payment = payment
        self.__status = status
        self.__code = code

    def proceed_payment(self):
        self.__payment.pay()
        self.__status = OrderStatus.CLOSE
