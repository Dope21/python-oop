from dataclasses import dataclass
from typing import List,Optional

from .Product import Product

@dataclass
class Category:
    name: str
    products: List[Product]

    def product_in_catagory_by_id(self,catename,id):
        for category in self.categories:
            if category.name== catename :
                for i in category.products:
                    if i.id==id:
                        return i
    def product_in_catagory_by_name(self,catename,name):
        for category in self.categories:
            if category.name== catename :
                for i in category.products:
                    if i.name==name:
                        return i
