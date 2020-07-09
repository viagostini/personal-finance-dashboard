from decimal import Decimal

from app.routers import transactions
from sqlalchemy.orm import Session

from ..schemas import schemas
from . import models

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + 'notreallyhashed'
    new_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user




def get_accounts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Account).offset(skip).limit(limit).all()


def create_account(db: Session, account: schemas.AccountCreate, user_id: int):
    new_account = models.Account(**account.dict(), owner_id=user_id)
    
    db.add(new_account)
    db.commit()
    db.refresh(new_account)

    return new_account


def create_transaction(
    db: Session, transaction: schemas.TransactionCreate, account_id: int
):
    def float_to_int(number: float) -> int:
        return int(Decimal(str(number)) * 100)
    
    transaction_dict = transaction.dict()
    transaction_dict['value'] = float_to_int(transaction_dict['value'])

    new_transaction = models.Transaction(
        **transaction_dict, account_id=account_id
    )


    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    return new_transaction


def get_transaction_by_id(db: Session, id: int):
    print(f'ID = {id}')
    return db.query(models.Transaction).filter(models.Transaction.id == id).first()

def get_transactions_from_account(
    db: Session,
    account_id: int,
    skip: int = 0,
    limit:int = 100
):
    return (db.query(models.Transaction)
              .filter(models.Transaction.account_id == account_id)
              .offset(skip).limit(limit).all())


def delete_transaction(db: Session, id: int):
    transaction = get_transaction_by_id(db, id)
    
    db.delete(transaction)
    db.commit()
    
    return transaction