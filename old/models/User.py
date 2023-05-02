from dataclasses import dataclass, field
from typing import Optional

from .Cart import Cart, CartItem

class User:
    def __init__(self, 
                 email = str, 
                 firstname = str,
                 lastname = str,
                 password = str ):
        
        self.__email = email
        self.__firstname = firstname
        self.__lastname = lastname
        self.__password = password

    def check_credential(self, email, password):
            return self.__email == email and self.__password == password
    
class Admin(User):
        def __init__(self, phone: str):
                self.__phone = phone
        
class Customer(User):
        def __init__(self, cart: Optional[Cart] = None):
                self.__cart = cart

        def add_cart_item(self, product, qty): 
                if not self.__cart:
                        self.__cart = Cart()
                return self.__cart.add_item(CartItem(product, qty))