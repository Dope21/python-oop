from fastapi import APIRouter

router = APIRouter()

from models.System import System
from models.Cart import Cart
from models.Product import *
from models.User import  *
from models.Category import *
@router.get("/add_product")
async def admin():
    system = System()
    category=Category
    
    
    system.add_categories(Category(name="K2"))
    system.add_categories(Category(name="K1",sub_list=["1","2","3"]))
   
    p1=system.find_category(name="K2")
    p1.sub_list=["1","2","3"]
    
    return p1