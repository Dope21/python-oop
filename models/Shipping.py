from enum import Enum
from dataclasses import dataclass

class ShippingMethod(Enum):
  STANDART = 0
  EMS = 1

@dataclass
class Shipping:
  tracking_no: str
  date: str
  method: ShippingMethod
  firstname: str
  lastname: str
  address: str
  phone: str
  zip_code: str

