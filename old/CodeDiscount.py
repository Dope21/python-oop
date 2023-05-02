from datetime import date


class CodeDiscount:
    def __init__(self, code: str, expire_date: date, discount: float):
        self.__code = code
        self.__expire_date = date
        self.__discount = discount

    def is_expire(self):
        return self.__expire_date > date.today()
