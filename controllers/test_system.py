from fastapi import APIRouter

router = APIRouter()

from models.System import System
from models.Cart import Cart

@router.get("/")
async def sign_in():
  system = System()

  email="test@gmail.com"
  password="password"
  firstname="firstname"
  lastname="lastname"
  
  customer = system.create_customer(email,password,firstname,lastname,Cart())

  result = system.sign_in(email=email,password=password)
  return result