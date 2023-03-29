from dataclasses import dataclass
from typing import List
# from Customer       import Customer
# from Admin          import Admin
# from Category       import Category
# from Subcategories import Subcategories
# from Product        import Product
# from Order          import Order
from CodeDiscount   import CodeDiscount

@dataclass
class Customer:
    def check_credential(self, email, passward):
        # do something with email, passward
        return "True or False"
    
class Admin:
    pass

class Product:
    pass

class Category:
    pass

class Subcategories:
    pass

class Order:
    class order_list:
        pass # have order in it!
    def is_history_of_(self, email):
        return "True or False"    

@dataclass
class System:
    customers: List[Customer]
    admins: List[Admin]
    categories: List[Category]
    subcategories: List[Subcategories]
    products: List[Product]
    orders: List[Order]
    codes: List[CodeDiscount]

    # @staticmethod function that not need self

    def create_customer(self, email, passward, firstname, lastname):
        customer = Customer(email, passward, firstname, lastname)
        status = self.customers.append(customer)
        return status

    def sign_up(self, email, passward, firstname, lastname):
        system = System()
        customer = system.create_customer(email, passward, firstname, lastname)
        status = self.customers.append(customer)
        return status
    
    def sign_in(self, email, passward):
        status = Customer.check_credential(email, passward)
        if status == True :
            return "Login completed"
        else:
            return "Wrong email or password"
            
    def get_order_history(self, email): ##!
        order_history_list = []
        for order in Order.order_list:
            status = order.is_history_of_(email)
            if status: order_history_list.append(order)
        return order_history_list
    