from pydantic import BaseModel


class Checkout(BaseModel):
    email: str
    firstname: str
    lastname: str
    pay_method: str
    address: str
    phone: str
    zip_code: str
    discount: float
    code: str


class Checkout(BaseModel):
    email: str
    firstname: str
    lastname: str
    pay_method: str
    address: str
    phone: str
    zip_code: str
    discount: float
    code: str
    pro_id: str
    cate_name: str


class CheckDiscount(BaseModel):
    code: str
