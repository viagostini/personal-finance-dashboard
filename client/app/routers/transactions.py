from typing import Optional
import requests, json

from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse

from .utils import service_api_url, templates

router = APIRouter()

@router.get('/new')
async def new_transaction(request: Request):
    return templates.TemplateResponse(
        'new_transaction.html',
        {"request": request}
    )

@router.post('/')
async def create_transaction(
    request: Request,
    account_id: int,
    title: str = Form(...),
    value: float = Form(...),
    category: str = Form("Other"),
    type: str = Form(...),
    description: Optional[str] = Form(None)
):
    response = requests.post(
        f'{service_api_url}/transactions/?account_id={account_id}',
        data=json.dumps({
            "title": title, "value": value,
            "category":category, "type":type,
            "description":description
        })
    )
    print(response.json())
    return RedirectResponse('http://localhost:8001/transactions/?user_id=1', status_code=303)



@router.get('/')
async def show_transactions_for_user(request: Request, user_id: int):
    user = requests.get(f'{service_api_url}/users/{user_id}').json()
    return templates.TemplateResponse(
        'transactions.html',
        {"request": request, "user": user}
    )


@router.post('/{id}')
async def delete_transaction_by_id(request: Request, id: int):
    response = requests.delete(f'{service_api_url}/transactions/{id}')
    print(response.json())
    return RedirectResponse('http://localhost:8001/transactions/?user_id=1', status_code=303)