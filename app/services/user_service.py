from fastapi import HTTPException, status
from db import async_session
from db.database import UserRepo
from core.security import to_hash_password
from api.schemas.user import UserReg
from db.models import User


async def registration_new_user(user_data: UserReg):
    async with async_session() as session:
        user_repo: UserRepo = UserRepo(session)
        user = await user_repo.get_user(user_data.username)
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User is already registered'
            )
        hash_password = to_hash_password(user_data.password)
        user = User(
            username=user_data.username,
            hash_password=hash_password,
            active=True
        )
        await user_repo.create_user(user)
