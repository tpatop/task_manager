from abc import ABC, abstractclassmethod
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from .models import User
from .models import Task


class Basic(ABC):
    def __init__(self, session_maker):
        self._session_maker = session_maker

    @property
    def session(self) -> AsyncSession:
        session = self._session_maker
        return session

    @abstractclassmethod
    async def get_all(self):
        ...

    @abstractclassmethod
    async def create_one(self):
        ...

    @abstractclassmethod
    async def get_one(self):
        ...

    @abstractclassmethod
    async def update_one(self):
        ...

    @abstractclassmethod
    async def delete_one(self):
        ...


class UserRepo(Basic):
    async def get_all(self):
        pass

    async def get_one(self, username: str):
        async with self.session as session:
            query = select(User).filter_by(username=username)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    async def create_one(self, user: User):
        async with self.session as session:
            session.add(user)
            try:
                await session.commit()
            except IntegrityError as exc:
                await session.rollback()
                raise exc

    async def update_one(self):
        pass

    async def delete_one(self, user: User):
        async with self.session as session:
            await session.delete(user)
            try:
                await session.commit()
            except IntegrityError as exc:
                await session.rollback()
                raise exc


class TaskRepo(Basic):
    async def get_all(self, user: User):
        async with self.session as session:
            query = select(Task).filter_by(user_id=user.user_id)
            result = await session.execute(query)
            return result.fetchall()

    async def get_one(self, user: User, task_id: int):
        async with self.session as session:
            query = select(Task).filter_by(user_id=user.user_id, id=task_id)
            result = await session.execute(query)
            return result.one_or_none()

    async def create_one(self, task: Task):
        async with self.session as session:
            session.add(task)
            try:
                await session.commit()
            except IntegrityError as exc:
                await session.rollback()
                raise exc

    async def update_one(self):
        pass

    async def delete_one(self, task: Task):
        async with self.session as session:
            await session.delete(task)
            try:
                await session.commit()
            except IntegrityError as exc:
                await session.rollback()
                raise exc
