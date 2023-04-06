from pydantic import BaseModel
from models.Product import Product
from models.Cart import CartItem
from typing import List


class SignInInfo(BaseModel):
  email: str
  password: str



class ProductSchema(BaseModel):
    def __init__(self, id, name, price, description, image, qty):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.image = image
        self.qty = qty

class CartItemSchema(BaseModel):
    product: ProductSchema 
    quantity: int

class CartSchema(BaseModel):
    cart_items: List[CartItemSchema] = []
