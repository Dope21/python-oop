from pydantic import BaseModel
from models.Product import Product

# Define the request body schema
class DiscountCode(BaseModel):
    code: str