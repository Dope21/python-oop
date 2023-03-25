from dataclasses import dataclass
from typing import list

class Admin:
    pass
class Customer:
    pass
class Product:
    pass
class Category:
    pass
class Order:
    pass
class Discount:
    pass

@dataclass
class System:
    admins: list(Admin)
    customers: list(Customer)
    categories: list(Category)
    products: list(Product)
    orders: list(Order)
    discounts: list(Discount)
