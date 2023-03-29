from dataclasses import dataclass, field
from typing import List, Optional

from .Cart import Cart
from .Address import Address

@dataclass
class User:
    id : str
    email : str
    firstname : str
    lastname : str
    password : str

    def check_credential(self, email, password):
            if self.email == email and self.password == password:
                    return True
            return False

@dataclass
class Admin(User):
        phone : str = field(default="10",metadata={"max_length":10})

@dataclass
class Customer(User):
        addresses: List[Address] = field(default_factory=list)
        cart: Optional[Cart] = None








