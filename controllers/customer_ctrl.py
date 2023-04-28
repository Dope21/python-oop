from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from init_system import system
from schemas.customer_shcema import SignIn, SignUp, AddCartItem, GetCart
from models.User import Customer
from models.Cart import Cart

from models.CodeDiscount import *

router = APIRouter(prefix="/customer")


@router.post("/sign_in")
async def customer_login(body: SignIn):
    try:
        customer = system.sign_in(body.email, body.password)
        if not customer:
            return JSONResponse(status_code=400, content="Wrong email or password.")
        return {"detail": "Successfully Sign-in", "data": customer.email}
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))


@router.post("/sign_up")
async def customer_register(body: SignUp):
    try:
        email = body.email
        password = body.password
        firstname = body.firstname
        lastname = body.lastname

        if system.get_customer_by_email(email):
            raise HTTPException(status_code=400, detail="This email already exist")

        system.add_customer(Customer(email, password, firstname, lastname, Cart()))
        return {"detail": "Successfully Sign-up"}

    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))


@router.post("/add_cart")
async def add_cart_item(body: AddCartItem):
    email = body.email
    item_id = body.cart_item.product_id
    qty = body.cart_item.qty

    customer = system.find_customer_by_email(email)
    product = system.find_product_by_id(item_id)

    if customer and product:
        customer.add_cart_item(product, qty)
        return {"message": "success"}
    else:
        raise HTTPException(status_code=400, detail="Something went wrong")


@router.get("/viewcart")
async def view_cart(body: GetCart):
    customer = system.get_customer_by_email(body.email)
    return customer.cart
