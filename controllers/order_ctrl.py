from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/order")

from init_system import system
from models.Order import Order, OrderItem, OrderStatus
from models.Shipping import Shipping
from schemas.order_shcema import CheckoutSchema

@router.post("/checkout")
async def checkout(checkout_info: CheckoutSchema):

  email = checkout_info.email
  pay_info = checkout_info.pay_info
  ship_info = checkout_info.ship_info
  discount = checkout_info.discount

  customer = system.get_customer_by_email(email)
  if not customer:
    raise HTTPException(status_code=400, detail=f"{email} is not exist")
  
  if not customer.cart:
    raise HTTPException(status_code=400, detail="No item in the cart")

  order_item_list = []
  for item in customer.cart.cart_items:
    order_item = OrderItem(item.product, item.qty, float("{:.2f}".format(item.product.price * discount)))
    order_item_list.append(order_item)
  
  payment = system.create_payment(pay_info.method, pay_info.name_on_card) 
  shipping = Shipping(ship_info.firstname, ship_info.lastname, ship_info.address, ship_info.phone, ship_info.zip_code)

  order = Order(order_item_list, OrderStatus.OPEN, shipping, payment, email)
  system.add_order(order)

  if order.process_payment(pay_info):
    return { "detail": "successful payment" }
  else:
    raise HTTPException(status_code=400, detail="Payment denied. Please try again later.")
  

# @router.post("/buynow")
# async def buynow(product_id: str, payment: PaymentSchema, shipping: ShippinpSchma):
  # pass

@router.post('/check_discount')
async def check_discount(discount_code: str):

    # Check if the code is valid
    if discount_code in system.codes: # code is parameter in function and second code is code in system.codes
         # Check if the code has expired
        if system.codes[discount_code].is_expired():
            # Raise an HTTP exception with an error message
            raise HTTPException(status_code=400, detail='Discount code has expired')
        else:
            # Return the discount amount
            discount = system.codes[discount_code].discount
            return {'status': 'success', 'discount': discount}
    else:
        # Raise an HTTP exception with an error message
        raise HTTPException(status_code=400, detail='Invalid discount code')
