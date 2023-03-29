from dataclasses import dataclass, field
from typing import List

from Address import Address,SetAddress

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
        address: List[Address] = field(default_factory=list)

        def check_credential(self, email, password):
            if self.email == email and self.password == password:
                return True
            else:
                return False

        def get_account_detail(self):
            return {'email': self.email, 'firstname': self.firstname, 'lastname': self.lastname}

        def get_addresses(self):
            return self.address

        def add_address(self, new_address):
            if isinstance(new_address, Address):
                self.address.append(new_address)
                return True
            else:
                return False

        def update_address(self, old_address, new_address):
            if old_address in self.address:
                self.address[self.address.index(old_address)] = new_address

                return True
            else:
                return False

        def delete_address(self, address):
            if address in self.address:
                self.address.remove(address)
    
                return True
            else:
                return False

        def create_address(self, *params):
            new_address = Address(*params)
            self.address.append(new_address)
            return True

customer = Customer(id='2', email='customer@example.com', firstname='Jane', lastname='Doe', password='password')


address1 = Address(firstname='Jane', lastname='Doe', address='123 Main St', phone='123-456-7890', zip_code='12345', set=SetAddress.MAIN)
customer.add_address(address1)


address2 = Address(firstname='Jane', lastname='Doe', address='456 Main St', phone='123-456-7890', zip_code='12345', set=SetAddress.OTHER)
customer.update_address(address1, address2)

print(customer.get_account_detail())
print(customer.get_addresses())












