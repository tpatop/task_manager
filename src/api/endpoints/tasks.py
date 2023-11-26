from typing import Annotated
from fastapi import APIRouter, Depends

from src.api.schemas.user import UserInDB
from src.api.schemas.task import Task
from src.core.security import get_current_active_user
from src.services.task_service import TaskServices


router = APIRouter()


@router.get('/list')
async def get_all(
    user: Annotated[UserInDB, Depends(get_current_active_user)]
):
    ts = TaskServices()
    task_list = await ts.get_user_tasks_list(user)
    if task_list:
        return task_list
    else:
        return {'message': 'No task found'}


@router.post('/create')
async def create_new_task(
    user: Annotated[UserInDB, Depends(get_current_active_user)],
    task_data: Task
):
    ts = TaskServices()
    await ts.add_user_task(user, task_data)
    return {'message': 'Task is added'}


@router.get('/get')
async def read_task(
    user: Annotated[UserInDB, Depends(get_current_active_user)],
    task_id: int
):
    ts = TaskServices()
    task = await ts.get_one_user_task(user, task_id)
    return task


# @router.post('/put')
# async def put_task():
#     pass


@router.post('/delete')
async def delete_one(
    user: Annotated[UserInDB, Depends(get_current_active_user)],
    task_id: int
):
    ts = TaskServices()
    await ts.delete_user_task(user, task_id)
    return {'message': 'Task is delete'}
