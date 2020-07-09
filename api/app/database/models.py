from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    accounts = relationship('Account', back_populates='owner')


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='accounts')
    transactions = relationship('Transaction', back_populates='account')


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, default='expense')
    value = Column(Integer, nullable=False)
    title = Column(String, nullable=False, index=True)
    description = Column(String)
    category = Column(String, default='Other')
    timestamp = Column(DateTime, default=datetime.now)
    account_id = Column(Integer, ForeignKey('accounts.id'))

    account = relationship('Account', back_populates='transactions')