from dataclasses import dataclass, field
from typing import List
from .User import Customer, Admin
from .Order import Order
from .Category import Category
from .CodeDiscount import CodeDiscount

@dataclass
class System:
    customers: List[Customer] = field(default_factory=list) 
    admins: List[Admin] = field(default_factory=list)
    categories: List[Category] = field(default_factory=list)
    orders: List[Order] = field(default_factory=list)
    codes: List[CodeDiscount] = field(default_factory=list)

    def sign_in(self, email, password):
        for customer in self.customers:
            if customer.email == email and customer.password == password:
                return True
        return False

    def add_customer(self, customer):
        if isinstance(customer, Customer):
            self.customers.append(customer)
            return True
        else:
            return False

    def add_admin(self, admin):
        if isinstance(admin, Admin):
            self.customers.append(admin)
            return True
        else:
            return False 
     
    def add_category(self, category):
        if isinstance(category, Category):
            self.customers.append(category)
            return True
        else:
            return False 

    def add_order(self, order):
        if isinstance(order, Order):
            self.customers.append(order)
            return True
        else:
            return False 
  
    def add_code_discount(self, code_discount):
        if isinstance(code_discount, CodeDiscount):
            self.customers.append(code_discount)
            return True
        else:
            return False