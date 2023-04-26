from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()
app = FastAPI()

from controllers import customer_ctrl
from controllers import order_ctrl
from controllers import product_ctrl

app.include_router(customer_ctrl.router)
app.include_router(order_ctrl.router)
app.include_router(product_ctrl.router)

origins = ["http://localhost", "http://localhost:5173", "http://127.0.0.1:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
