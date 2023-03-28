from pydantic import BaseModel
from typing import List

# testing
from models.Order import Product

class Shippinp(BaseModel):
  tracking_no: str
  date: str
  method: str
  firstname: str
  lastname: str
  address: str
  phone: str
  zip_code: str

class OrderItem(BaseModel):
  product: Product
  qty: int
  price: float

class ItemList(BaseModel):
  items_list: List[OrderItem]

class Payment(BaseModel):
  card_number: str
  name_on_card: str
  expired_date: str
  code: str
  method: str

  