from dataclasses import dataclass
from enum import Enum
from typing import Optional

class PaymentStatus(Enum):
  Unpaid = 0
  Paid = 1
  
@dataclass
class Payment:
  transection_id: Optional[str]
  date: Optional[str]
  status: PaymentStatus

class Paypal(Payment):
  pass

@dataclass
class CreditCard(Payment):
  name_on_card: str
