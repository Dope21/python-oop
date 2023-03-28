from dataclasses import dataclass
from typing import List
# from Customer       import Customer
# from Admin          import Admin
# from Category       import Category
# from Product        import Product
# from Order          import Order
from CodeDiscount   import CodeDiscount
@dataclass
class Customer:
    def create_customer(self, email, passward, firstname, lastname):
        # do something with email, passward, firstname, lastname
        return "Create customer completed"
    def check_credential(self, email, passward):
        # do something with email, passward
        return "True or False"
    
class Admin:
    pass

class Product:
    pass

class Category:
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
    products: List[Product]
    orders: List[Order]
    codes: List[CodeDiscount]

    def sign_up(self, email, passward, firstname, lastname):
        status = Customer.create_customer(email, passward, firstname, lastname)
        return status
    
    def sign_in(self, email, passward):
        status = Customer.check_credential(email, passward)
        if status == True :
            return "Login completed"
        else:
            raise # return "Wrong email or password"
            
    def get_order_history(self, email): ##!
        order_history_list = []
        for order in Order.order_list:
            status = order.is_history_of_(email)
            if status: order_history_list.append(order)
        return order_history_list
    