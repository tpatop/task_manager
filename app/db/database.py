from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from api.models.user import UserInDB
from .models import User


class Basic:
    def __init__(self, session_maker):
        self._session_maker = session_maker

    @property
    def session(self) -> AsyncSession:
        session = self._session_maker
        return session


class UserRepo(Basic):
    async def get_user(self, username: str):
        async with self.session as session:
            query = select(User).filter_by(username=username)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    async def create_user(self, user: User):
        async with self.session as session:
            session.add(user)
            try:
                await session.commit()
            except IntegrityError as exc:
                await session.rollback()
                raise exc


    async def update_user(self, ):
        pass

    async def delete_user(self, ):
        pass
