from dataclasses import dataclass
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
class Customer(User):
        address:List[Address]



class Admin(User):
        phone : int












