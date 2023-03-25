from dataclasses import dataclass
from typing import List
from User import User
from Address import Address

@dataclass
class Customer(User):
        address:List[Address]