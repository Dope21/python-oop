from dataclasses import dataclass
from typing import List

from .User import Customer, Admin
from .Order import Order
from .Product import Product
from .Category import Category, SubCategory
from .CodeDiscount import CodeDiscount

@dataclass
class System:
    customers: List[Customer]
    admins: List[Admin]
    categories: List[Category]
    orders: List[Order]
    codes: List[CodeDiscount]

    # CUSTOMER MANAGEMENT
    def create_customer(self, email, passward, firstname, lastname):
        customer = Customer(email, passward, firstname, lastname)
        status = self.customers.append(customer)
        return status

    def sign_in(self, email, password):
        for customer in self.customers:
            if customer.check_credential(email, password):
                return True
        return False 
         
    def get_order_history(self, email): 
        order_history_list = []
        for order in self.orders:
            if order.is_history_of(email):
                order_history_list.append(order) 
        return order_history_list