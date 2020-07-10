import requests

from fastapi import APIRouter, Request

from .utils import service_api_url, templates

router = APIRouter()

@router.get('/')
async def show_all_users(request: Request):
    users = requests.get(f'{service_api_url}/users/').json()
    return templates.TemplateResponse(
        'users.html',
        {"request": request, "users": users}
    )

@router.get('/{id}')
async def show_user(request: Request, id: int):
    user = requests.get(f'{service_api_url}/users/{id}').json()
    return templates.TemplateResponse(
        'user.html',
        {"request": request, "id": user['id']}
    )