from .Cart import Cart


class User:
    def __init__(self, email: str, password: str, firstname: str, lastname: str):
        self.__email = email
        self.__password = password
        self.__firstname = firstname
        self.__lastname = lastname

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password


class Admin(User):
    def __init__(
        self, email: str, password: str, firstname: str, lastname: str, phone: str
    ):
        super().__init__(email, password, firstname, lastname)
        self.__phone = phone


class Customer(User):
    def __init__(
        self,
        email: str,
        password: str,
        firstname: str,
        lastname: str,
        cart: Cart,
    ):
        super().__init__(email, password, firstname, lastname)
        self.__cart = cart
        self.__orders = []
