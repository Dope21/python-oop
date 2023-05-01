from .User import Customer
from .Cart import Cart
from .Category import Category


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

    # category
    def get_category_by_name(self, name):
        for cate in self.__categories:
            if cate.name == name:
                return cate
        raise ValueError("Invalid Category name.")

    def create_category(self, name):
        category = Category(name)
        self.add_category(category)
        return category

    def add_category(self, category):
        if isinstance(category, Category):
            self.__categories.append(category)
        else:
            raise ValueError("Please add Category object.")
