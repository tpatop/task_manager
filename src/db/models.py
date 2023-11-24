from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import (
    Column, Integer, String, Boolean, DateTime, ForeignKey
)
from datetime import datetime


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    hash_password = Column(String)
    active = Column(Boolean, default=True)
    # tasks = relationship('Task', backref='user_id')


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    detail = Column(String, nullable=True)
    active = Column(Boolean, default=True)
    dt_create = Column(DateTime(timezone=True), default=datetime.now)
    dt_redline = Column(DateTime(timezone=True), nullable=True, default=None)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship('User', backref='tasks', foreign_keys=[user_id])
