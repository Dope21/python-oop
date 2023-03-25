from dataclasses import dataclass
from enum import Enum

class PaymentStatus(Enum):
  Unpaid = 0
  Paid = 1
  
@dataclass
class Payment:
  transection_id: str
  date: str
  status: PaymentStatus

class Paypal(Payment):
  pass

@dataclass
class CreditCard(Payment):
  name_on_card: str
