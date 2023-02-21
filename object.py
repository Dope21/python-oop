# from enum import Enum

# class OrderStatus(Enum):
#     Waiting = 0
#     Confirm = 1

# class PaymentStatus(Enum):
#     Waiting = 0
#     Finish = 1

# class SetAddress(Enum):
#     Main = 1
#     Other = 0

# class Account:
#     def __init__(self, id, password, user):
#         self.__id = id
#         self.__password = password
#         self.__user = user
    
# class User():
#     def __init__(self, email, firstname, lastname):
#         self.__email = email
#         self.__firstname = firstname
#         self.__lastname = lastname

# class Address:
#     def __init__(self, firstname, lastname, phone="", address="", zip_code="", set=SetAddress.Main):
#         self.__firstname = firstname
#         self.__lastname = lastname
#         self.__phone = phone
#         self.__address = address
#         self.__zip_code = zip_code
#         self.__set = set

# class Customer(User):
#     def __init__(self, email, firstname, lastname):
#         super().__init__(email, firstname, lastname)
#         self.__addresses = [Address(firstname, lastname)]
#         self.__cart = Cart()

# class Admin(User):
#     def __init__(self, email, firstname, lastname, phone):
#         super().__init__(email, firstname, lastname)
#         self.__phone = phone

# class Product:
#     def __init__(self, name, description, price, quantity, image, category):        
#         self.__name = name
#         self.__description = description
#         self.__price = price
#         self.__quantity = quantity
#         self.__image = image
#         self.__category = category

# class Keyboard(Product):
#     def __init__(self, name, description, price, quantity, image, category, version, type, switches, color):
#         super().__init__(name, description, price, quantity, image, category)
#         self.__version = version
#         self.__type = type
#         self.__switches = switches
#         self.__color = color

# class Mouse(Product):
#     def __init__(self, name, description, price, quantity, image, category, connection, color):
#         super().__init__(name, description, price, quantity, image, category)
#         self.__connection = connection
#         self.__color = color

# class Switch(Product):
#     def __init__(self, name, description, price, quantity, image, category, option, quantity_set):
#         super().__init__(name, description, price, quantity, image, category)
#         self.__option = option
#         self.__quantity_set = quantity_set

# class Keycap(Product):
#     def __init__(self, name, description, price, quantity, image, category, version, color):
#         super().__init__(name, description, price, quantity, image, category)
#         self.__version = version
#         self.__color = color

# class Category:
#     def __init__(self, name):
#         self.__name = name
        
# class Catalog:
#     def __init__(self):
#         self.__products = []

# class Cart:
#     def __init__(self):
#         self.__items = []
   
# class CartItem:
#     def __init__(self, quantity, product):
#         self.__quantity = quantity
#         self.__product = product

# class OrderItem(CartItem):
#     def __init__(self, price, quantity, product):
#         super().__init__(quantity, product)
#         self.__price = price

# class Order:
#     def __init__(self, order_id, status, order_items=[], code_discount=""):
#         self.__order_id = order_id
#         self.__status = status
#         self.__order_items = order_items
#         self.__code_discounts = code_discount

# class CodeDiscount:
#     def __init__(self, code, discount, expire_date):
#         self.__code = code
#         self.__discount = discount
#         self.__expire_date = expire_date

# class Payment:
#     def __init__(self, transection_id, date, status):
#         self.__transection_id = transection_id
#         self.__date = date
#         self.__status = status

# class CreditCard(Payment):
#     def __init__(self, transection_id, date, status, name_on_card):
#         super().__init__(transection_id, date, status)
#         self.__name_on_card = name_on_card

# class MobileBanking(Payment):
#     def __init__(self, transection_id, date, status):
#         super().__init__(transection_id, date, status)
        
# class Shipping:
#     def __init__(self, tracking_no, method, date, address):
#         self.__tracking_no = tracking_no
#         self.__method = method
#         self.__date = date
#         self.__address = address