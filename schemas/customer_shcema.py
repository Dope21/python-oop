from pydantic import BaseModel
from models.Product import Product

class SignInInfo(BaseModel):
  email: str
  password: str

class CartItem(BaseModel):
  product_id: str
  qty: int