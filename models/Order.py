from dataclasses import dataclass
from typing import List, Union, Optional
from enum import Enum

from Payment import Paypal, CreditCard, PaymentStatus
from Shipping import Shipping, ShippingMethod

@dataclass
class Product:
  name: str
  price: int
  
class OrderStatus(Enum):
  OPEN = 0
  CLOSE = 1

@dataclass
class OrderItem:
  product: Product
  qty: int
  price: Optional[float] = 0

@dataclass
class Order:
  items: List[OrderItem]
  status: OrderStatus
  shipping: Shipping
  payment: Union[Paypal,CreditCard]
  email: str

# Testing
item1 = OrderItem(product=Product(name="something", price=750), qty=1)
item2 = OrderItem(product=Product(name="something", price=750), qty=1)

address = Shipping(
  tracking_no="number",
  date="today", 
  method=ShippingMethod.EMS, 
  firstname="thanasak", 
  lastname="limsila", 
  address="some where in the world",
  phone="number",
  zip_code="1293"
)
payment = Paypal(status=PaymentStatus.Paid, date="today", transection_id="alkejiofahe")
order = Order(items=[item1, item2], status=OrderStatus.CLOSE, shipping=address, payment=payment)
print(order)