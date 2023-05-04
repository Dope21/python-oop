from fastapi import APIRouter, HTTPException
from schemas.order_shcema import CheckDiscount, Checkout
from init_system import system

router = APIRouter(prefix="/order")


@router.post("/get_discount")
def get_discount_code(body: CheckDiscount):
    try:
        code = body.code

        discount = system.get_discount_code(code)
        if discount.is_expire():
            raise ValueError("This code is already expired.")
        return {"data": discount.get_detail()}
    except ValueError as e:
        raise HTTPException(detail=str(e), status_code=400)
    except Exception as e:
        raise HTTPException(detail=str(e), status_code=500)


@router.post("/checkout")
def checkout(body: Checkout):
    try:
        email = body.email
        firstname = body.firstname
        lastname = body.lastname
        address = body.address
        phone = body.phone
        zip_code = body.zip_code
        code = body.code
        discount = body.discount
        pay_method = body.pay_method

        customer = system.get_customer_by_email(email)

        customer.create_order_checkout(
            firstname,
            lastname,
            address,
            phone,
            zip_code,
            code,
            discount,
            pay_method,
        )

        return {"detail": "Your order had been created."}

    except ValueError as e:
        raise HTTPException(detail=str(e), status_code=400)
    except Exception as e:
        raise HTTPException(detail=str(e), status_code=500)


@router.post("/buynow")
def checkout(body: Checkout):
    try:
        email = body.email
        firstname = body.firstname
        lastname = body.lastname
        address = body.address
        phone = body.phone
        zip_code = body.zip_code
        code = body.code
        discount = body.discount
        pay_method = body.pay_method
        pro_id = body.pro_id
        cate_name = body.cate_name

        customer = system.get_customer_by_email(email)
        category = system.get_category_by_name(cate_name)
        product = category.get_product_by_id(pro_id)

        customer.create_order_buynow(
            firstname,
            lastname,
            address,
            phone,
            zip_code,
            code,
            discount,
            pay_method,
            product,
        )

        return {"detail": "Your order had been created."}

    except ValueError as e:
        raise HTTPException(detail=str(e), status_code=400)
    except Exception as e:
        raise HTTPException(detail=str(e), status_code=500)
