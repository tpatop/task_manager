from typing import Annotated
from fastapi import APIRouter, Depends

from src.api.schemas.user import UserInDB
from src.api.schemas.task import Task
from src.core.security import get_current_active_user
from src.services.task_service import (
    get_user_tasks_list,
    get_one_user_task,
    add_user_task,
    delete_user_task
)


router = APIRouter()


@router.get('/list')
async def get_tasks_list(
    user: Annotated[UserInDB, Depends(get_current_active_user)]
):
    task_list = await get_user_tasks_list(user)
    return task_list


@router.post('/create')
async def create_new_task(
    user: Annotated[UserInDB, Depends(get_current_active_user)],
    task_data: Task
):
    await add_user_task(user, task_data)
    return {'message': 'Task is added'}


@router.get('/get')
async def read_task(
    user: Annotated[UserInDB, Depends(get_current_active_user)],
    task_id: int
):
    task = await get_one_user_task(user, task_id)
    return task


# @router.post('/put')
# async def put_task():
#     pass


@router.post('/delete')
async def delete_task(
    user: Annotated[UserInDB, Depends(get_current_active_user)],
    task_id: int
):
    await delete_user_task(user, task_id)
    return {'message': 'Task is delete'}
