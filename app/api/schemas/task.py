from pydantic import BaseModel
from typing import Union
from datetime import datetime


class Task(BaseModel):
    name: str
    detail: str
    dt_create: datetime
    dt_redline: Union[datetime, None]


class TaskResponce(Task):
    id: int
    active: bool
    user_id: int
