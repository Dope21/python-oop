from fastapi import APIRouter, HTTPException
from init_system import system
from schemas.product_shcema import CateName, FindById

router = APIRouter(prefix="/product")


@router.post("/product_in_category")
async def get_product_in_category(body: CateName):
    try:
        cate_name = body.cate_name
        category = system.get_category_by_name(cate_name)

        product_list = []
        for product in category.products:
            product_list.append(product.get_detail())
            product_list[-1]["category"] = cate_name
        return {"data": product_list}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get_all_product")
async def get_all_product():
    try:
        product_list = []
        for cate in system.categories:
            for p in cate.products:
                product_list.append(p.get_detail())
                product_list[-1]["category"] = cate.name
        return {"data": product_list}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/detail")
async def get_product_detail(body: FindById):
    try:
        pro_id = int(body.pro_id)
        cate_name = body.cate_name

        category = system.get_category_by_name(cate_name)
        product = category.get_product_by_id(pro_id)

        return {"data": product.get_detail()}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
