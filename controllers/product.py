from fastapi import APIRouter

router = APIRouter()
from models.System import System
from models.Product import *
from models.Category import *
from init_system import *

@router.get("/all_catagory")
async def admin():
    res = system.list_category()
    return res

@router.get("/all_catagory_name")
async def admin():
    res = system.list_category_name()
    return res
@router.get("/catagory_by_name")
async def admin():
    res = system.find_category_by_name("cateTest1")
    return res
@router.get("/all_product_in_catagory_by_name")
async def admin():
    res = system.all_product_in_catagory("cateTest1")
    return res
@router.get("/product_in_catagory_by_id")
async def admin():
    res = system.product_in_catagory_by_id("cateTest1","001")
    return res
@router.get("/product_in_catagory_by_name")
async def admin():
    res = system.product_in_catagory_by_name("cateTest1","K2 SSR")
    return res

