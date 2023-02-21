class User:
    def __init__(self, email, firstname, lastname, password):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password

class Address:
    def __init__(self, firstname, lastname, phone="", address="", zip_code="", set=False):
        self.frstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.address = address
        self.zip_code = zip_code
        self.set = set

    def change_information(self):
        pass

class Customer(User):
    def __init__(self, email, firstname, lastname, password):
        super().__init__(email, firstname, lastname, password)
        self.addresses = [Address(firstname=firstname, lastname=lastname, set=True)]

class Admin(User):
    def __init__(self, email, firstname, lastname, password):
        super().__init__(email, firstname, lastname, password)
        self.phone = ""

class AccountManager:

    def __init__(self):
        pass

    def create_customer(self, email, firstname, lastname, password):
        pass

    def create_admin(self, email, firstname, lastname, password):
        pass

    def email_existed(self, email):
        pass

    @staticmethod
    def validate_signup(email, firstname, lastname, password):
        pass
            













