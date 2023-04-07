from pydantic import BaseModel
<<<<<<< HEAD
from typing import Optional
=======
from typing import List
from models.Product import Product
>>>>>>> 1551b5e4aa630be81bbc6241c8fdfbba8b0e648d

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

<<<<<<< HEAD
class CheckoutSchema(BaseModel):
  email: str
  pay_info: Payment
  ship_info: Shippinp
  discount: Optional[float] = 1
=======


>>>>>>> 1551b5e4aa630be81bbc6241c8fdfbba8b0e648d

  