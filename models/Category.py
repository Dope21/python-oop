from dataclasses import dataclass
from typing import List

from .Product import Product

@dataclass
class Category:
    name: str
    products: List[Product]

