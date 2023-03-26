from dataclasses import dataclass
from typing import List
from System import Product

@dataclass
class Cartitem:
    product: Product
    quantity: int

    def set_quantity(self, quantity):
        self.quantity = quantity

@dataclass
class Cart:
    cartitems: List[Cartitem]
    
# method list
    def get_cart(self):
        return self.cartitems
