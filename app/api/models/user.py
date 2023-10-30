from pydantic import BaseModel


class User(BaseModel):
    username: str


class UserReg(User):
    password: str


class UserInDB(User):
    hash_password: str
    active: bool = True
