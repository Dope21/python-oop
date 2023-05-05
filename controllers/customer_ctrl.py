from fastapi import APIRouter, HTTPException
from init_system import system
from schemas.customer_shcema import SignIn, SignUp, SetCart, Email
from models.Cart import CartItem

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


@router.post("/set_cart_item")
async def add_cart_item(body: SetCart):
    try:
        email = body.email
        product_list = body.product_list

        customer = system.get_customer_by_email(email)
        if not customer:
            raise ValueError("There is no customer with this email.")
        cart = customer.cart

        cart_items = []
        for item in product_list:
            category = system.get_category_by_name(item.category)
            product = category.get_product_by_id(item.id)
            cart_items.append(CartItem(product, item.quantity))

        cart.cart_items = cart_items

        return {"detail": "Successfully added."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/get_cart_detail")
async def view_cart(body: Email):
    try:
        email = body.email

        customer = system.get_customer_by_email(email)
        if not customer:
            raise ValueError("There is no customer with this email.")
        cart = customer.cart

        return {"data": cart.get_detail()}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
