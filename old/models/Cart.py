from .Product import *


class CartItem:
    def __init__(self, product: Product, qty: int):
        self.__product = product
        self.__qty = qty

    @property
    def product(self):
        return self.__product

    @property
    def qty(self):
        return self.__qty


class Cart:
    def __intit__(self):
        self.__cart_items = []

    def add_item(self, item):
        if isinstance(item, CartItem):
            self.cart_items.append(item)
            return True
        raise Exception("Please add CartItem object.")

    def remove_item(self, item):
        if item in self.__cart_items:
            self.__cart_items.remove(item)
