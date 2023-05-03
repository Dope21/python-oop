from .Product import *
from .Order import OrderItem


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

    def get_detail(self):
        detail = self.__product.get_detail()
        detail["qty"] = self.__qty
        return detail


class Cart:
    def __init__(self):
        self.__cart_items = []

    @property
    def cart_items(self):
        return self.__cart_items

    @cart_items.setter
    def cart_items(self, item_list):
        for item in item_list:
            if not isinstance(item, CartItem):
                raise ValueError("Please add CartItem object")
        self.__cart_items = item_list

    def get_detail(self):
        return [item.get_detail() for item in self.__cart_items]

    def create_order_items(self, discount):
        order_items = []
        for item in self.__cart_items:
            order_items.append(
                OrderItem(
                    item.product, item.qty, round(item.product.price * discount, 2)
                )
            )
        return order_items
