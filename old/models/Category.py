from dataclasses import dataclass
from typing import List

from .Product import Product

@dataclass
class Category:
    name: str
    products: List[Product]

    def get_product_by_id(self, id):
        for product in self.products:
            if id == product.id:
                return product
        return False

    def get_product_by_name(self, name):
        for product in self.products:
            if name == product.name:
                return product
     