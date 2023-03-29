from dataclasses import dataclass, field
from typing import List, Optional

from .User import Customer, Admin
from .Address import Address, SetAddress
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

    # CUSTOMER MANAGEMENT
    def create_customer(self, email, password, firstname, lastname):
        address = [Address(firstname=firstname, lastname=lastname, set=SetAddress.MAIN)]
        customer = Customer(id= "someid",email=email, password=password, firstname=firstname, lastname=lastname, address=address)
        self.customers.append(customer)
        return customer

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