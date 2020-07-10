from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from .routers import users, transactions
from .routers.utils import templates

import requests

app = FastAPI()

@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


app.include_router(users.router, prefix='/users', tags=['users'])
app.include_router(transactions.router, prefix='/transactions', tags=['transactions'])