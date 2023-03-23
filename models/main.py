
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
        self.cart = []
    def add_address(self,address):
        self.addresses.append(address)
    def add_cart(self,carts):
        self.cart.append(carts)


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

class Cart:
    def __init__(self,product,quantity,cartitems:list):
       super().__init__(self,product,quantity)
       self.cartitems = []
    def add_item(self,cartitem):
        self.cartitems.append(cartitem)

class CartItem():
    def __init__(self,product,quantity:int):
        self.project = product
        self.quantity = quantity







