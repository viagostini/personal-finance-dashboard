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


@router.get('/', response_model=List[schemas.Transaction])
def get_transactions_from_account(
    account_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_transactions_from_account(
        db=db,
        account_id=account_id,
        skip=skip,
        limit=limit
    )

@router.get('/{id}', response_model=schemas.Transaction)
def get_transaction_by_id(id: int, db: Session = Depends(get_db)):
    return crud.get_transaction_by_id(db=db, id=id)


@router.delete('/{id}', response_model=schemas.Transaction)
def delete_transaction(id: int, db: Session = Depends(get_db)):
    return crud.delete_transaction(db=db, id=id)
