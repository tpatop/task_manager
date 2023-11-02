from pydantic import BaseModel
from typing import Union
from datetime import datetime


class Task(BaseModel):
    id: int
    name: str
    detail: str
    dt_create: datetime
    dt_redline: Union[datetime, None]
    active: bool
    user_id: int
