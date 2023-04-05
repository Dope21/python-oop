from fastapi import APIRouter

router = APIRouter()

from init_system import system
from schemas.order_shcema import ItemList, Item, Payment, Shippinp

@router.post("/order/checkout")
async def checkout(item_list: ItemList, payment: Payment, shipping: Shippinp):
  pass

@router.post("order/buynow")
async def buynow(item: Item, payment: Payment, shipping: Shippinp):
  pass

