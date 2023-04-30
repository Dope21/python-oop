from fastapi import APIRouter, HTTPException
from init_system import system
from schemas.customer_shcema import SignIn, SignUp, AddCartItem, GetCart

router = APIRouter(prefix="/customer")


@router.post("/sign_in")
async def customer_login(body: SignIn):
    try:
        return {
            "detail": "Successfully Sign-in",
            "data": system.sign_in(body.email, body.password),
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/sign_up")
async def customer_register(body: SignUp):
    try:
        email = body.email
        password = body.password
        firstname = body.firstname
        lastname = body.lastname

        customer = system.create_customer(email, password, firstname, lastname)
        return {"detail": "Successfully Sign-up", "data": customer.email}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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
