from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def Hello():
    return "hello world"

# command for running API
# uvicorn main:app --reload
