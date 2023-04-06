from fastapi import FastAPI,APIRouter
router = APIRouter()
app = FastAPI()

from controllers import product
from controllers import customer_ctrl
app.include_router(product.router)
app.include_router(customer_ctrl.router)