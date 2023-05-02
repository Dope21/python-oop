from fastapi import APIRouter, HTTPException
from init_system import system
from schemas.product_shcema import CateName

router = APIRouter(prefix="/product")


@router.post("/product_in_category")
async def get_product_in_category(body: CateName):
    try:
        cate_name = body.cate_name
        category = system.get_category_by_name(cate_name)

        product_list = [p.get_detail() for p in category.products]
        return {"data": product_list}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get_all_category")
async def get_all_category():
    try:
        return {
            "data": [
                p.get_detail() for cate in system.categories for p in cate.products
            ]
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
