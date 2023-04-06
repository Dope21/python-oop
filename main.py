from fastapi import FastAPI

app = FastAPI()

# from controllers import customer_ctrl
# app.include_router(customer_ctrl.router)

# from controllers import product
# app.include_router(product.router)

from controllers import discount_ctrl
app.include_router(discount_ctrl.router)