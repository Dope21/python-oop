class Product:
    def __init__(self, id, name, price, description, image, qty):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__description = description
        self.__image = image
        self.__qty = qty

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def description(self):
        return self.__description

    @property
    def image(self):
        return self.__image

    @property
    def qty(self):
        return self.__qty


class Keyboard(Product):
    def __init__(
        self,
        id,
        name,
        price,
        description,
        image,
        qty,
        version,
        type,
        switches,
        color,
    ):
        super().__init__(id, name, price, description, image, qty)
        self.__version = version
        self.__type = type
        self.__switches = switches
        self.__color = color

    def get_detail(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "image": self.image,
            "qty": self.qty,
            "version": self.__version,
            "type": self.__type,
            "switches": self.__switches,
            "color": self.__color,
        }


############################################################# Mouse ###########################################################


class Mouse(Product):
    def __init__(self, id, name, price, description, image, qty, connection, color):
        super().__init__(id, name, price, description, image, qty)
        self.__connection = connection
        self.__color = color

    def get_detail(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "image": self.image,
            "qty": self.qty,
            "connection": self.__connection,
            "color": self.__color,
        }


########################################################### Switch ########################################


class Switch(Product):
    def __init__(
        self,
        id,
        name,
        price,
        description,
        image,
        qty,
        option,
        quantity_set,
    ):
        super().__init__(id, name, price, description, image, qty)
        self.__option = option
        self.__quantity_set = quantity_set

    def get_detail(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "image": self.image,
            "qty": self.qty,
            "option": self.__option,
            "quantity_set": self.__quantity_set,
        }


########################################################### Keycap ########################################


class Keycap(Product):
    def __init__(self, id, name, price, description, image, qty, version, color):
        super().__init__(id, name, price, description, image, qty)
        self.__version = version
        self.__color = color

    def get_detail(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "image": self.image,
            "qty": self.qty,
            "version": self.__version,
            "color": self.__color,
        }
