from dataclasses import dataclass
from System import Product

@dataclass
class Cartitem:
    product: Product
    quantity: int

@dataclass
class Cart:
    cartitems: list[Cartitem]
    
    def add_cart():
        pass

    def remove_item():
        pass

    def edit_quantity():
        pass