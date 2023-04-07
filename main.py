from fastapi import FastAPI

app = FastAPI()

from controllers import customer_ctrl
from controllers import order_ctrl

app.include_router(customer_ctrl.router)
app.include_router(order_ctrl.router)