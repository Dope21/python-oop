from dataclasses import dataclass
from enum import Enum
from typing import List

class DiscountStatus(Enum):
    INACTIVE = 0
    ACTIVE   = 1

@dataclass
class OrderItem():
    pass

@dataclass
class CodeDiscount():
    orderitems: List[OrderItem]
    status: DiscountStatus
