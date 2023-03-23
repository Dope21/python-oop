from Product import *
class Switch(Product):
    def __init__(self,id:str,name:str,price:float,description:str,image:str,last_update:str,option:str,quantity_set:int):
        self.__id= id
        self.__name=name
        self.__price=price
        self.__description=description
        self.__image=image
        self.__last_update=last_update
        self.__option=option
        self.__quantity_set=quantity_set

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def get_description(self):
        return self.__description
    def get_image(self):
        return self.__image
    def get_last_update(self):
        return self.__last_update
    def get_option(self):
        return self.__option
    def get_quantity_set(self):
        return self.__quantity_set
    
    def set_id(self,id:str):
        self.__id= id
    def set_name(self,name:str):
        self.__name= name
    def set_price(self,price:str):
        self.__price= price
    def set_description(self,description:str):
        self.__description= description
    def set_image(self,image:str):
        self.__image= image
    def set_last_update(self,last_update:str):
        self.__last_update= last_update
    def set_option(self,option:str):
        self.__option= option
    def set_quantity_set(self,quantity_set:str):
        self.__quantity_set= quantity_set