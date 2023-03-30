from dataclasses import dataclass, field
from typing import List

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
    def create_customer(self, email, password, firstname, lastname, cart):
        address = [Address(firstname=firstname, lastname=lastname, set=SetAddress.MAIN)]
        customer = Customer(firstname=firstname,lastname=lastname,password=password,email=email, addresses=address, cart=cart)
        self.add_customer(customer=customer)
        return customer
    
    def check_duplicate_email(self, email):
        for customer in self.customers:
           if customer.email == email:
               return True 
        return False

    def sign_in(self, email, password):
        for customer in self.customers:
            if not customer.check_credential(email, password):
                continue
            else: 
                return True
        return False 
         
    def get_order_history(self, email): 
        order_history_list = []
        for order in self.orders:
            if order.is_history_of(email):
                order_history_list.append(order) 
        return order_history_list
    
    def add_customer(self, customer):
        if isinstance(customer, Customer):
            self.customers.append(customer)
            return True
        else:
            return False 