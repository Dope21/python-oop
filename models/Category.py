from dataclasses import dataclass
from typing import List,Optional

from .Product import Product

@dataclass
class BaseCategory:
    name: str
@dataclass
class SubCategory(BaseCategory):
    products: List[Product]
    
    
@dataclass
class Category(BaseCategory):
    sub_list: Optional[List[SubCategory]]=None
    
    def add_subcategory(self,subcategory):
        self.sub_list.append(subcategory)
    def list_sub(self):
        list = []
        for i in self.sub_list:
            list.append(i)
        return list
    
    
        

