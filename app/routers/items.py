from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schemas import schemas
from ..database import crud
from ..database.database import get_db


router = APIRouter()


@router.post('/', response_model=schemas.Item)
def create_item(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_item(db=db, item=item, user_id=user_id)


@router.get('/', response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db=db, skip=skip, limit=limit)
    return items