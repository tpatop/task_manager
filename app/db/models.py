from sqlalchemy.orm import declarative_base
from sqlalchemy import (
    Column, Integer, String, Boolean
)


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    username = Column(String, primary_key=True)
    hash_password = Column(String)
    active = Column(Boolean, default=True)


# class Task(Base):
#     __tablename__ = 'tasks'
