from dataclasses import dataclass
from typing import List

from .Product import Product

@dataclass
class BaseCategory:
    name: str

class SubCategory(BaseCategory):
    products: List[Product]

class Category(BaseCategory):
    sub_list: List[SubCategory]

