from fastapi import APIRouter, HTTPException

router = APIRouter()

from models.CodeDiscount import *
from schemas.discount_schema import DiscountCode
from init_system import system

@router.post('/check_discount')
async def check_discount(discount_code: DiscountCode):
    # Check if the code is valid
    if discount_code.code in system.codes: # code is parameter in function and second code is code in system.codes
         # Check if the code has expired
        if system.codes[discount_code.code].is_expired():
            # Raise an HTTP exception with an error message
            raise HTTPException(status_code=400, detail='Discount code has expired')
        else:
            # Return the discount amount
            discount = system.codes[discount_code.code].discount
            return {'status': 'success', 'discount': discount}
    else:
        # Raise an HTTP exception with an error message
        raise HTTPException(status_code=400, detail='Invalid discount code')
