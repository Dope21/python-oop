from dataclasses import dataclass
from datetime import date

class OrderItem():
    pass

@dataclass
class CodeDiscount():
    code: str
    expire_date: date

    def is_expire(self):
        return self.expire_date > date.today()