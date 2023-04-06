from pydantic import BaseModel
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
