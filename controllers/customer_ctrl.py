from fastapi import APIRouter, HTTPException

router = APIRouter()

from init_system import system
from schemas.customer_shcema import SignInInfo, CartItem

@router.get("/get_all")
async def get_all_customer():
  return { "data": system.customers }

@router.post("/sign_in")
async def customer_login(signInInfo: SignInInfo):
  customer = system.sign_in(signInInfo.email, signInInfo.password)
  if not customer:
   raise HTTPException(status_code=400, detail="Wrong email or password")

  return { "message": "Sign in successful", "data": customer }

@router.post("/add_cart")
async def add_cart_item(email: str, cart_item: CartItem):
  customer = system.find_customer_by_email(email)
  product = system.find_product_by_id(cart_item.product_id)

  if customer and product:
    customer.add_cart_item(product, cart_item.qty)
    return { "message": "successs" }
  else:
    raise HTTPException(status_code=400, detail="Something went wrong")

  