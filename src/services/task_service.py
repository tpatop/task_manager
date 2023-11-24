from typing import List
from fastapi import HTTPException, status

from src.db.session import async_session
from src.db.database import TaskRepo, UserRepo, User, Task
from src.api.schemas.user import UserInDB
from src.api.schemas.task import Task as TaskShemas


async def get_user_tasks_list(user: UserInDB):
    async with async_session() as session:
        user_repo: UserRepo = UserRepo(session)
        user_model: User = await user_repo.get_user(user.username)
        task_repo: TaskRepo = TaskRepo(session)
        task_list = await task_repo.get_tasks_list(user_model)
        task_list: List[User] = [lst[0] for lst in task_list]

        if task_list:
            return task_list
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='No tasks found!'
            )


async def add_user_task(user: UserInDB, task_data: TaskShemas):
    async with async_session() as session:
        user_repo: UserRepo = UserRepo(session)
        user_model: User = await user_repo.get_user(user.username)
        task_repo: TaskRepo = TaskRepo(session)

        task_data = task_data.model_dump()
        task_data['user_id'] = user_model.user_id
        task: Task = Task(**task_data)
        await task_repo.create_task(task)


async def get_one_user_task(user: UserInDB, task_id: int):
    async with async_session() as session:
        user_repo: UserRepo = UserRepo(session)
        user_model: User = await user_repo.get_user(user.username)
        task_repo: TaskRepo = TaskRepo(session)

        task = await task_repo.get_task(user_model, task_id)
        if task:
            return task[0]
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='A task with the specified parameters was not found!'
            )


async def delete_user_task(user: UserInDB, task_id: int):
    async with async_session() as session:
        task: Task = await get_one_user_task(user, task_id)
        print(task)
        task_repo: TaskRepo = TaskRepo(session)

        await task_repo.delete_task(task)
