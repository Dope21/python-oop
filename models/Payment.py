from enum import Enum
from datetime import date
import random
import string


class PaymentStatus(Enum):
    UNPAID = 0
    PAID = 1


class Payment:
    def __init__(self):
        self.__status = PaymentStatus.UNPAID
        self.__date = None
        self.__transection_id = None

    def pay(self):
        self.__status = PaymentStatus.PAID
        self.__date = date.today()
        self.__transection_id = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=10)
        )


class Paypal(Payment):
    pass


class CreditCard(Payment):
    pass
