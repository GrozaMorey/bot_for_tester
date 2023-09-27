from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, BigInteger, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime

PATH_TO_DB = "postgresql://postgres:123@localhost/postgres"

engine = create_engine(PATH_TO_DB)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    pay_in_mouth = Column(Boolean, default=False)
    chat_id = Column(Integer, default=None)
    expired = Column(Date, nullable=True)
    number_badge = Column(Integer, nullable=True)
    update_badge = Column(Date, nullable=True)

    transaction = relationship("Transaction", backref="owner")
    success_transaction = relationship("SuccessTransaction", backref="owner")


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    transaction_id = Column(BigInteger)
    date = Column(Date, default=datetime.datetime.now())

    user = relationship("User", backref="payment")


class SuccessTransaction(Base):
    __tablename__ = "success_transaction"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    telegram_payment_charge_id = Column(String)
    provider_payment_charge_id = Column(String)
    date = Column(Date, default=datetime.datetime.now())

    user = relationship("User", backref="success_payment")


Session = sessionmaker(bind=engine)
session = Session()
