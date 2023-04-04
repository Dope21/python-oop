from dataclasses import dataclass, field
from typing import Optional

from .Cart import Cart

@dataclass
class User:
    email : str
    firstname : str
    lastname : str
    password : str

    def check_credential(self, email, password):
            return self.email == email and self.password == password
@dataclass
class Admin(User):
        phone : str = field(default="10",metadata={"max_length":10})
        
@dataclass
class Customer(User):
        cart: Optional[Cart] = None