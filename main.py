from fastapi import FastAPI

app = FastAPI()

from controllers import customer_ctrl
<<<<<<< HEAD
from controllers import order_ctrl

app.include_router(customer_ctrl.router)
app.include_router(order_ctrl.router)
=======
app.include_router(customer_ctrl.router)

from controllers import product
app.include_router(product.router)

from controllers import discount_ctrl
app.include_router(discount_ctrl.router)
>>>>>>> c955283428770f5239e3aa83fed571bdbc947429
