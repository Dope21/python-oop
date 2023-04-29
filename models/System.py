from .User import Customer, Admin
from .Order import Order
from .Category import Category
from .CodeDiscount import CodeDiscount
from .Payment import CreditCard, Paypal, PaymentStatus


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
                return customer
        return False

    def add_customer(self, customer):
        if isinstance(customer, Customer):
            self.__customers.append(customer)
            return True
        raise Exception("Please add Customer object.")

    def add_admin(self, admin):
        if isinstance(admin, Admin):
            self.__customers.append(admin)
            return True
        else:
            return False

    def add_category(self, category):
        if isinstance(category, Category):
            self.__categories.append(category)
            return True
        else:
            return False

    def add_order(self, order):
        if isinstance(order, Order):
            self.__orders.append(order)
            return True
        else:
            return False

    def add_code_discount(self, code_discount):
        if isinstance(code_discount, CodeDiscount):
            self.__codes.append(code_discount)
            return True
        else:
            return False

    # Finding Object
    def get_customer_by_email(self, email):
        for customer in self.__customers:
            if email == customer.__email:
                return customer
        return False

    def find_product_by_id(self, product_id):
        for category in self.__categories:
            product = category.get_product_by_id(product_id)
            if product:
                return product
        return False

    def find_product_by_name(self, product_name):
        for category in self.__categories:
            product = category.get_product_by_name(product_name)
            if product:
                return product
        return False

    def find_category_by_name(self, category_name):
        for category in self.__categories:
            if category.name == category_name:
                return category
        return False

    def find_discount_code(self, discount_code):
        for code in self.__codes:
            if code.code == discount_code:
                return code
        return False

    # create payment
    def create_payment(self, method, name_on_card):
        if method == "credit-card":
            return CreditCard(name_on_card=name_on_card, status=PaymentStatus.Unpaid)
        else:
            return Paypal(name_on_card=name_on_card, status=PaymentStatus.Unpaid)

    def get_all_category(self):
        return self.__categories

    def get_category_name(self):
        list = []
        for category in self.__categories:
            list.append(category.name)
        return list
