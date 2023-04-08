from pydantic import BaseModel
from typing import Optional

class Shippinp(BaseModel):
  firstname: str
  lastname: str
  address: str
  phone: str
  zip_code: str

class ItemList(BaseModel):
  id: str
  qty: int

class Payment(BaseModel):
  card_number: str
  name_on_card: str
  expired_date: str
  code: str
  method: str

class CheckoutSchema(BaseModel):
  email: str
  pay_info: Payment
  ship_info: Shippinp
  discount: Optional[float] = 1

class CodeSchema(BaseModel):
  code: str