from fastapi import APIRouter

router = APIRouter()
from models.Product import *
from models.Category import *
from init_system import *

@router.get("/all_catagory")
async def admin():
    return system.categories

@router.get("/all_catagory_name")
async def admin():
    return system.list_category_name()

@router.get("/catagory_by_name")
async def admin():
    res = system.find_category_by_name("cateTest1")
    return res

@router.get("/all_product_in_catagory_by_name")
async def admin():
    category = system.find_category_by_name(name)
    name_list = category.get_all_product_name()
    return name_list

@router.get("/product_in_catagory_by_id")
async def admin():
    res = system.find_product_by_id()
    return res

@router.get("/product_in_catagory_by_name")
async def admin():
    res = system.product_in_catagory_by_name("cateTest1","K2 SSR")
    return res