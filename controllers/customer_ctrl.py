from fastapi import APIRouter, HTTPException
from init_system import system
from schemas.customer_shcema import SignInInfo, CartItemSchema, ProductSchema, CartSchema
from models.Cart import Cart, CartItem
from models.Product import Product

router = APIRouter()

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
async def add_cart_item(email: str, cart_item: CartItemSchema):
    customer = system.find_customer_by_email(email)
    product = Product(name=cart_item.product.name, price=cart_item.product.price)
    if customer and product:
        item = CartItem(product=product, quantity=cart_item.quantity)
        customer.cart.add_item(item)
        return { "message": "success" }
    else:
        raise HTTPException(status_code=400, detail="Something went wrong")

@router.get("/cart", response_model=CartSchema)
async def view_cart(email: str):
    customer = system.find_customer_by_email(email)
    my_cart = Cart()
    if customer and customer.cart:
        my_cart = customer.cart
    return CartSchema(cart_items=[CartItemSchema(product=ProductSchema(name=item.product.name, price=item.product.price), quantity=item.quantity) for item in my_cart.get_cart()])
