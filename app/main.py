from app.routers import transactions
from fastapi import FastAPI

from .database import models
from .routers import transactions, accounts, users
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
    accounts.router,
    prefix="/accounts",
    tags=["accounts"]
)
app.include_router(
    transactions.router,
    prefix="/transactions",
    tags=["transactions"]
)