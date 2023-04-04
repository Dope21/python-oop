from fastapi import FastAPI

app = FastAPI()

<<<<<<< HEAD
from controllers import api_system, test_system

# testing router
app.include_router(test_system.router)
=======
from controllers import customer_ctrl

app.include_router(customer_ctrl.router)
>>>>>>> 751e626684844737a1ffd6f4d8dd5e03e9c6758d
