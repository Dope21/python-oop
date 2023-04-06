from pydantic import BaseModel
from models.Product import Product
from models.Cart import CartItem
from typing import List


class SignInInfo(BaseModel):
  email: str
  password: str



class ProductSchema(BaseModel):
    name: str
    price: float

class CartItemSchema(BaseModel):
    product: ProductSchema 
    quantity: int

class CartSchema(BaseModel):
    cart_items: List[CartItemSchema] = []
