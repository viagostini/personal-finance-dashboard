from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

import requests

app = FastAPI()

service_api_url = 'http://localhost:8000'

templates = Jinja2Templates(directory="client/templates")

@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})

@app.get('/users/')
async def show_all_users(request: Request):
    users = requests.get(f'{service_api_url}/users/').json()
    return templates.TemplateResponse(
        'users.html',
        {"request": request, "users": users}
    )

@app.get('/users/{id}')
async def show_user(request: Request, id: int):
    user = requests.get(f'{service_api_url}/users/{id}').json()
    return templates.TemplateResponse(
        'user.html',
        {"request": request, "id": user['id']}
    )

@app.get('/users/{id}/transactions')
async def show_transactions_for_user(request: Request, id: int):
    user = requests.get(f'{service_api_url}/users/{id}').json()
    return templates.TemplateResponse(
        'transactions.html',
        {"request": request, "user": user}
    )