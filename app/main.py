from fastapi import FastAPI

from .database import models
from .routers import items, users
from .database.database import engine

# creates the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def index():
    return {"msg": "Hello!"}

app.include_router(
    users.router,
    prefix="/users",
    tags=["users"]
)
app.include_router(
    items.router,
    prefix="/items",
    tags=["items"]
)
