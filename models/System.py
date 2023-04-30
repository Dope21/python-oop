from .User import Customer, Admin
from .Order import Order
from .Cart import Cart


class System:
    def __init__(self):
        self.__customers = []
        self.__admins = []
        self.__categories = []
        self.__orders = []
        self.__codes = []

    # customer
    def sign_in(self, email, password):
        for customer in self.__customers:
            if customer.check_credential(email, password):
                return customer.email
        raise ValueError("Wrong email or password.")

    def add_customer(self, customer):
        if isinstance(customer, Customer):
            self.__customers.append(customer)
        else:
            raise ValueError("Please add Customer object.")

    def get_customer_by_email(self, email):
        for customer in self.__customers:
            if email == customer.email:
                return customer

    def create_customer(self, email, password, firstname, lastname):
        if self.get_customer_by_email(email):
            raise ValueError("This email in already in use.")
        customer = Customer(email, password, firstname, lastname, Cart())
        self.add_customer(customer)
        return customer
