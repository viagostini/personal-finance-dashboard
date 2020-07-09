from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schemas import schemas
from ..database import crud
from ..database.database import get_db


router = APIRouter()


@router.post('/', response_model=schemas.Account)
def create_account(
    user_id: int, account: schemas.AccountCreate, db: Session = Depends(get_db)
):
    return crud.create_account(db=db, account=account, user_id=user_id)


@router.get('/', response_model=List[schemas.Account])
def read_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    accounts = crud.get_accounts(db=db, skip=skip, limit=limit)
    return accounts