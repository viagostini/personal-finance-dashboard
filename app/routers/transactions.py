from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schemas import schemas
from ..database import crud
from ..database.database import get_db


router = APIRouter()


@router.post('/', response_model=schemas.Transaction)
def create_transaction(
    account_id: int,
    transaction: schemas.TransactionCreate,
    db: Session = Depends(get_db)
):
    return crud.create_transaction(
        db=db,
        transaction=transaction,
        account_id=account_id
    )