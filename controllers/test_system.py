from fastapi import APIRouter

router = APIRouter()

from models.System import System
from models.Cart import Cart
from models.Address import Address, SetAddress

@router.get("/")
async def sign_in(product):
  system = System()
  
  product = Product(product)
  status = system.add_product(product)

  return 