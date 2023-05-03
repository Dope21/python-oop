from datetime import date


class CodeDiscount:
    def __init__(self, code: str, expire_date: date, discount: float):
        self.__code = code
        self.__expire_date = expire_date
        self.__discount = discount

    @property
    def code(self):
        return self.__code

    def is_expire(self):
        return date.today() > self.__expire_date

    def get_detail(self):
        return {"code": self.__code, "discount": self.__discount}
