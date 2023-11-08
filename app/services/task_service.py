from typing import List
from db.session import async_session
from db.database import TaskRepo, UserRepo, User, Task
from api.schemas.user import UserInDB
from api.schemas.task import Task as TaskShemas


async def get_user_tasks_list(user: UserInDB):
    async with async_session() as session:
        user_repo: UserRepo = UserRepo(session)
        user_model: User = await user_repo.get_user(user.username)
        task_repo: TaskRepo = TaskRepo(session)
        task_list = await task_repo.get_tasks_list(user_model)
        task_list: List[User] = [lst[0] for lst in task_list]
        return task_list


async def add_user_task(user: UserInDB, task_data: TaskShemas):
    async with async_session() as session:
        user_repo: UserRepo = UserRepo(session)
        user_model: User = await user_repo.get_user(user.username)
        task_repo: TaskRepo = TaskRepo(session)

        task_data = task_data.model_dump()
        task_data['user_id'] = user_model.user_id
        print(task_data)
        task: Task = Task(**task_data)
        print(type(task), task)
        await task_repo.create_task(task)
