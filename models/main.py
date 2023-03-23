class User:
    def __init__(self,id:str,email: str,firstname:str,lastname:str,password:str):
        self.id = id
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
class Customer(User):
    def __init__(self,id:str,email:str,firstname:str,lastname:str,password:str,addresses:list):
        super().__init__(id,email, firstname, lastname, password)
        self.addresses = []
        self.addresses.append(addresses)


class Admin(User):
    def __init__(self,id:str,email:str,firstname:str,lastname:str,password:str,phone:str):
        super().__init__(id,email,firstname,lastname,password)
        self.phone = phone


class Address:
    def __init__(self, firstname: str, lastname: str, phone: str, address: str, zip_code: str):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.address = address
        self.zip_code = zip_code










