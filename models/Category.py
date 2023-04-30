from .Product import *


class Category:
    def __init__(self, name):
        self.__name = name
        self.__product = []

    @property
    def name(self):
        return self.__name

    def create_product(self, **kwargs):
        data = kwargs
        if len(self.__product) != 0:
            pro_id = self.__product[-1].id + 1
        else:
            pro_id = 1

        if data.kind == "keyboard":
            product = Keyboard(
                pro_id,
                data.name,
                data.price,
                data.description,
                data.image,
                data.qty,
                data.version,
                data.type,
                data.switches,
                data.color,
            )
        elif data.kind == "keycap":
            product = Keycap(
                pro_id,
                data.name,
                data.price,
                data.description,
                data.image,
                data.qty,
                data.version,
                data.color,
            )
        elif data.kind == "switch":
            product = Switch(
                pro_id,
                data.name,
                data.price,
                data.description,
                data.image,
                data.qty,
                data.option,
                data.quantity_set,
            )
        else:
            product = Mouse(
                pro_id,
                data.name,
                data.price,
                data.description,
                data.image,
                data.qty,
                data.connection,
                data.color,
            )
        self.add_product(product)
        return product

    def add_product(self, product):
        if isinstance(product, Product):
            self.__product.append(product)
        else:
            raise ValueError("Please add Product object.")
