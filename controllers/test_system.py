from fastapi import APIRouter

router = APIRouter()

from models.System import System
from models.Cart import Cart
from models.Product import *
from models.User import  *
@router.get("/")
async def sign_in():
  system = System()
  
  email="test@gmail.com"
  password="password"
  firstname="firstname"
  lastname="lastname"
  email2="test2@gmail.com"
  password2="password"
  firstname2="firstname"
  lastname2="lastname"
  #p1 = keyboard(id="001",name="K2 SSR",price=3200,description="A mechanical keyboard with RGB backlight",image="sefaf.png",version="v4",type="wireless",switches="blue switches",color="backlight")
  
  
  
  system.add_customer(Customer(email=email,password=password,firstname=firstname,lastname=lastname,addresses=[])) # create_customer ok
  system.add_customer(Customer(email=email,password=password,firstname=firstname,lastname=lastname,addresses=[]))
  #result = system.sign_in(email=email,password=password) # sign_in ok
  #chk = system.check_duplicate_email(email=email2) # check_duplicate_email ok
  #get_order_history = system.get_order_history(email=email)
  return system.list_customers() 
  