from dataclasses import dataclass
from typing import List

# dummy product
@dataclass
class Product:
   name: str
   price: float 

@dataclass
class CartItem:
    product: Product 
    quantity: int

    def get_product(self):
        return self.product

    def set_product(self, product):
        self.product = product

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, qty):
        self.qty = qty

@dataclass
class Cart:
    cart_items: List[CartItem]
    
    def get_cart(self):
        return self.cart_items
    
    def add_item(self, item):
        self.cart_items.append(item)
    
    def remove_item(self, item):
        if item in self.cart_items:
            self.cart_items.remove(item)