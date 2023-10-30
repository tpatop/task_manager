from datetime import timedelta
from datetime import datetime
from typing import Annotated
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from api.models.user import UserInDB
from db.database import get_user
from core.config import load_config, Config


config: Config = load_config()

SECRET_KEY = config.secret_key
ALGORITHM = config.algorithm
EXPIRE_MINUTES = config.expire_minutes


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# OAuth2PasswordBearer для авторизации по токену
# 'token' ~ './token' - путь до конечной точки, в
#  которой реализована аутентфикация
oauth2_sheme = OAuth2PasswordBearer(tokenUrl='/users/token')


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hash_password):
        return False
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_sheme)]):
    exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise exc
    except JWTError:
        raise exc
    user = get_user(username)
    if user is None:
        raise exc
    return user


async def get_current_active_user(
    current_user: Annotated[UserInDB, Depends(get_current_user)]
):
    if not current_user.active:
        raise HTTPException(status_code=400, detail='Inactive user')
    return current_user


def create_access_token(data: dict):
    to_encode = data.copy()
    # добавление времени жизни токена
    if EXPIRE_MINUTES:
        expire = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    # создание токена
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
