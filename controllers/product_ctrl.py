from fastapi import APIRouter,HTTPException

router = APIRouter()
from models.Product import *
from models.Category import *
from init_system import *
from schemas.product_shcema import *
        
@router.get("/all_catagory")
async def all_catagory():
    return { "data": system.get_category() } 

@router.get("/all_catagory_name")
async def all_catagory_name():
    return { "data": system.get_category_name() }
    
@router.post("/product_by_catename")
async def product_by_catename(body: CateName):
    category = system.find_category_by_name(category_name=body.cate_name)
    if not category:
        raise HTTPException(status_code=400, detail="Can not find category")
    return { "data": category.products } 

@router.post("/product_detail_by_id")
async def product_detail_by_id(body: ProId):
    product = system.find_product_by_id(body.id)
    if product:
        return { "data": product }
    raise HTTPException(status_code=400, detail="Can not find product")

@router.post("/product_detail_by_name")
async def product_detail_by_name(body: ProName):
    product = system.find_product_by_name(body.name)
    if product: 
        return { "data": product }  
    raise HTTPException(status_code=400, detail="Can not find product")

