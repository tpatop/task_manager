from pydantic import BaseModel


class User(BaseModel):
    username: str


class UserReg(User):
    password: str


class UserInDB(User):
    hash_password: str
    active: bool = True

    # # добавляем настройки для Pydantic
    # class Config:
    #     # позволяет обращаться не как к словарю, а к атрибуту класса
    #     orm_mode = True
