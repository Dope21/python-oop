from fastapi import APIRouter, HTTPException

router = APIRouter()

from models.CodeDiscount import *
from schemas.discount_schema import DiscountCode
from init_system import DISCOUNT_CODES # sample discount code

@router.post('/check_discount')
async def check_discount(code: DiscountCode):
    # Check if the code is valid
    if code.code in DISCOUNT_CODES: 
         # Check if the code has expired
        if DISCOUNT_CODES[code.code].is_expired():
            # Raise an HTTP exception with an error message
            raise HTTPException(status_code=400, detail='Discount code has expired')
        else:
            # Return the discount amount
            discount = DISCOUNT_CODES[code.code].discount
            return {'status': 'success', 'discount': discount}
    else:
        # Raise an HTTP exception with an error message
        raise HTTPException(status_code=400, detail='Invalid discount code')

