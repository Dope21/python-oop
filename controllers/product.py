from fastapi import APIRouter,HTTPException

router = APIRouter()
from models.System import System
from models.Product import *
from models.Category import *
from init_system import *
from schemas.product_shcema import *

        
@router.post("/all_catagory")
async def all_catagory():
    return { "data": system.list_category() } 

@router.post("/all_catagory_name")
async def all_catagory_name():
    return { "data": system.list_category_name() }
    

    
############## วิ่งไปดึง Product ทั้งหมดของ catagory ที่มีชื่อตามที่ต้องการจาก System
@router.post("/product_by_catename")
async def product_by_catename(name:Categoryname):
    res = system.find_category_by_name(category_name=name.catename)
    return res.products
        
   
    
    
############## วิ่งไปดึง catagory ที่มีชื่อตามที่ต้องการจาก System แล้วเข้าไปดูรายละเอียดของ Product
@router.post("/product_detail_by_id")
async def product_detail_by_id(productname:Proid):
    cate = system.find_category_by_name(category_name=productname.catename)
    for i in cate.products :
        if i.id == productname.id :
            return i
        

       
     

@router.post("/product_detail_by_name")
async def product_detail_by_name(productname:Proname):
    cate = system.find_category_by_name(category_name=productname.catename)
    for i in cate.products :
        if i.name == productname.name :
            return i
        

