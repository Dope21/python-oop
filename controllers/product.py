from fastapi import APIRouter

router = APIRouter()
from models.System import System
from models.Product import *
from models.Category import *
from init_system import *


        
@router.get("/all_product")
async def admin():
    res = system.list_category()
    return res

@router.get("/product_by_name")
async def admin():
    res = system.find_category_by_name("cateTest1")
    return res

