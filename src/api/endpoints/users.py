from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from src.api.schemas.token import Token
from src.api.schemas.user import UserReg
from src.core.security import (
    OAuth2PasswordRequestForm,
    authenticate_user,
    create_access_token,
    # get_current_active_user
)
from src.services.user_service import UserServices


router = APIRouter()


@router.post('/token', response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    user = await authenticate_user(
        form_data.username,
        form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    access_token = create_access_token(data={'sub': user.username})

    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/registration')
async def registration_user(user_data: UserReg):
    us = UserServices()
    await us.registration_new_user(user_data)
    return {'message': 'Successfull registration'}


# @router.get('/me', dependencies=[Depends(get_current_active_user)])
# async def get_me():
#     return {'message': 'Successfull'}
