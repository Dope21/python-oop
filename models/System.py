from dataclasses import dataclass
from typing import List

from User import Customer, Admin
from Order import Order
from CodeDiscount import CodeDiscount

class Product:
    pass
class Category:
    pass

@dataclass
class System:
    customers: List[Customer]
    admins: List[Admin]
    categories: List[Category]
    products: List[Product]
    orders: List[Order]
    codes: List[CodeDiscount]
