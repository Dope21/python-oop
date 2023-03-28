from dataclasses import dataclass, field
from typing import List

from Address import Address

@dataclass
class User:
    id : str
    email : str
    firstname : str
    lastname : str
    password : str

@dataclass
class Admin(User):
        phone : str = field(default="10",metadata={"max_length":10})

@dataclass
class Customer(User):
        address:List[Address]












