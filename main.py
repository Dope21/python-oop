from fastapi import FastAPI

app = FastAPI()

from controllers import customer_ctrl

app.include_router(customer_ctrl.router)