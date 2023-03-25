from dataclasses import dataclass
from typing import List
# from Customer       import Customer
# from Admin          import Admin
# from Category       import Category
# from Product        import Product
# from Order          import Order
from CodeDiscount   import CodeDiscount

class Customer:
    pass
class Admin:
    pass
class Product:
    pass
class Category:
    pass
class Order:
    pass

@dataclass
class System:
    customers: List[Customer]
    admins: List[Admin]
    categories: List[Category]
    products: List[Product]
    orders: List[Order]
    codes: List[CodeDiscount]
