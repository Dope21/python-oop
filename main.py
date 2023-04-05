from fastapi import FastAPI

app = FastAPI()

from controllers import product

app.include_router(product.router)