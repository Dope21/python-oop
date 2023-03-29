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
    
    def get_address_detail(self):
        return {'firstname': self.firstname, 'lastname': self.lastname, 'address': self.address,
                'phone': self.phone, 'zip_code': self.zip_code, 'set': self.set.name}
