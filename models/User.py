from .Cart import Cart
from models.Payment import *
from models.Shipping import Shipping
from models.Order import *


class User:
    def __init__(self, email: str, password: str, firstname: str, lastname: str):
        self.__email = email
        self.__password = password
        self.__firstname = firstname
        self.__lastname = lastname

    def check_credential(self, email, password):
        return self.__email == email and self.__password == password

    @property
    def email(self):
        return self.__email


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

    @property
    def cart(self):
        return self.__cart

    def create_order_checkout(
        self,
        firstname,
        lastname,
        address,
        phone,
        zip_code,
        code,
        discount,
        pay_method,
    ):
        order_items = self.cart.create_order_items(discount)
        shipping = Shipping(firstname, lastname, address, phone, zip_code)
        if pay_method == "paypal":
            payment = Paypal()
        if pay_method == "credit-card":
            payment = CreditCard()

        order = Order(
            self.email, order_items, shipping, payment, OrderStatus.OPEN, code
        )
        self.__orders.append(order)
        self.__cart.clear_cart()
        order.proceed_payment()
        return order

    def create_order_buynow(
        self,
        firstname,
        lastname,
        address,
        phone,
        zip_code,
        code,
        discount,
        pay_method,
        product,
    ):
        order_item = OrderItem(product, 1, product.price * discount)
        shipping = Shipping(firstname, lastname, address, phone, zip_code)
        if pay_method == "paypal":
            payment = Paypal()
        if pay_method == "credit-card":
            payment = CreditCard()

        order = Order(self.email, order_item, shipping, payment, OrderStatus.OPEN, code)
        self.__orders.append(order)
        order.process_payment()
        return order
