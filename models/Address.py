from dataclasses import dataclass
from enum import Enum

@dataclass
class SetAddress(Enum):
    OTHER = 0
    MAIN = 1
    
@dataclass
class Address:
    firstname : str
    lastname : str
    address : str
    phone : str
    zip_code : str
    set: SetAddress

