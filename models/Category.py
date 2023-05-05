from .Product import *


class Category:
    def __init__(self, name):
        self.__name = name
        self.__products = []

    @property
    def name(self):
        return self.__name

    @property
    def products(self):
        return self.__products

    def create_product(self, **kwargs):
        data = kwargs
        if len(self.__products) != 0:
            pro_id = self.__products[-1].id + 1
        else:
            pro_id = 1

        if data["kind"] == "keyboard":
            product = Keyboard(
                pro_id,
                data["name"],
                data["price"],
                data["description"],
                data["image"],
                data["qty"],
                data["version"],
                data["type"],
                data["switches"],
                data["color"],
            )
        elif data["kind"] == "keycap":
            product = Keycap(
                pro_id,
                data["name"],
                data["price"],
                data["description"],
                data["image"],
                data["qty"],
                data["version"],
                data["color"],
            )
        elif data["kind"] == "switch":
            product = Switch(
                pro_id,
                data["name"],
                data["price"],
                data["description"],
                data["image"],
                data["qty"],
                data["option"],
                data["quantity_set"],
            )
        else:
            product = Mouse(
                pro_id,
                data["name"],
                data["price"],
                data["description"],
                data["image"],
                data["qty"],
                data["connection"],
                data["color"],
            )
        self.__products.append(product)
        return product

    def get_product_by_id(self, id):
        for product in self.__products:
            if product.id == id:
                return product
        raise ValueError("There is no Product with this ID.")
