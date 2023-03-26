from dataclasses import dataclass
from typing import List
from System import Product

@dataclass
class CartItem:
    product: str # is {"Product"} Class
    quantity: int

    def get_product(self):
        return self.product

    def set_product(self, product):
        self.product = product

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

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

# test objects/methods
item1 = CartItem('example1', 2)
item2 = CartItem('example2', 3)

cart = Cart([])
cart.add_item(item1)
cart.add_item(item2)
print(cart.cart_items)

cart.remove_item(item1)
print(cart.cart_items)

cart.add_item(item=item1)
print(cart.cart_items)

item1.set_quantity(10)
print(cart.cart_items)

item1.set_product('new_product_name')
print(cart.cart_items)

print(item1.get_product())