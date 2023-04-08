from pydantic import BaseModel
from typing import List


class SignInInfo(BaseModel):
  email: str
  password: str

class CartItemSchema(BaseModel):
    product_id: str 
    qty: int

