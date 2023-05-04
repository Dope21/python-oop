from pydantic import BaseModel
from typing import List


class SignIn(BaseModel):
    email: str
    password: str


class SignUp(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str


class CartItem(BaseModel):
    product_id: str
    qty: int


class Item(BaseModel):
    id: int
    quantity: int
    category: str


class SetCart(BaseModel):
    email: str
    product_list: List[Item]


class Email(BaseModel):
    email: str
