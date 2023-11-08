from typing import Annotated
from fastapi import APIRouter, Depends

from api.schemas.user import UserInDB
from api.schemas.task import Task
from core.security import get_current_active_user
from services.task_service import (
    get_user_tasks_list,
    add_user_task
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


@router.post('/get')
async def read_task():
    pass


@router.post('/put')
async def add_new_task():
    pass


@router.post('/delete')
async def delete_task():
    pass
