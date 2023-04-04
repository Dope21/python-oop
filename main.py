from fastapi import FastAPI

app = FastAPI()

from controllers import api_system, test_system

# testing router
app.include_router(test_system.router)
