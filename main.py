from fastapi import FastAPI

app = FastAPI()

from controllers import Admin

# testing router
app.include_router(Admin.router)