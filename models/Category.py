from dataclasses import dataclass
from typing import List,Optional

from .Product import Product

@dataclass
class Category:
    name: str
    products: List[Product]

