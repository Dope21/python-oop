from dataclasses import dataclass
from datetime import date
from typing import List

class OrderItem():
    pass

@dataclass
class CodeDiscount():
    orderitems: List[OrderItem]
    expire_date: date

    def is_valid(self):
        return self.expire_date > date.today()
    
# test class
discount = CodeDiscount(10, date(2023, 1, 1))
print(discount)

if discount.is_valid():
    print("Discount is still valid")
else:
    print("Discount has expired")