from datetime import datetime

from typing import List, Optional

from pydantic import BaseModel

from ..database import models


class TransactionBase(BaseModel):
    title: str
    value: float
    description: Optional[str]


class TransactionCreate(TransactionBase):
    type: Optional[str]
    category: Optional[str]
    # timestamp: Optional[datetime]

class Transaction(TransactionBase):
    id: int
    type: str
    category: str
    account_id: int
    # timestamp: datetime

    def from_orm(obj):
        return Transaction(
            id=obj.id,
            title=obj.title,
            description=obj.description,
            category=obj.category,
            type=obj.type,
            account_id=obj.account_id,
            # timestamp=obj.timestamp,
            value=obj.value / 100
        )

    class Config:
        orm_mode = True
        orm_model = models.Transaction




class AccountBase(BaseModel):
    name: str


class AccountCreate(AccountBase):
    pass


class Account(AccountBase):
    id: int
    owner_id: int
    transactions: List[Transaction]

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    accounts: List[Account] = []

    class Config:
        orm_mode = True

