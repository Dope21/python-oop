from dataclasses import dataclass
from typing import Optional
from enum import Enum

@dataclass
class SetAddress(Enum):
    OTHER = 0
    MAIN = 1
    
@dataclass
class Address:
    firstname : str
    lastname : str 
    set: SetAddress
    address : Optional[str] = ""
    phone : Optional[str] = ""
    zip_code : Optional[str] = ""

