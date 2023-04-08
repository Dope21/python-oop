from dataclasses import dataclass
from datetime import date

@dataclass
class CodeDiscount():
    _code: str
    _expire_date: date
    _discount: float

    @property
    def code(self):
        return self._code
    
    @property
    def discount(self):
        return self._discount

    def is_expire(self):
        if not self._expire_date:
            return True
        return self._expire_date > date.today()