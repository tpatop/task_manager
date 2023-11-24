from fastapi import HTTPException, status
from src.db.session import async_session
from src.db.database import UserRepo
from src.core.security import to_hash_password
from src.api.schemas.user import UserReg
from src.db.models import User


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
