from fastapi import FastAPI

app = FastAPI()

<<<<<<< HEAD
<<<<<<< HEAD
from controllers import api_system, test_system

# testing router
app.include_router(test_system.router)
=======
from controllers import customer_ctrl

app.include_router(customer_ctrl.router)
>>>>>>> 751e626684844737a1ffd6f4d8dd5e03e9c6758d
=======
from controllers import product

app.include_router(product.router)
>>>>>>> 8a8dfbb28c0bc4a3768c88f9e03e9000537f0a67
