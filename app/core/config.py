from environs import Env
from pydantic import BaseModel


class Config(BaseModel):
    secret_key: str
    algorithm: str
    expire_minutes: int | None = None


class DBConfig(BaseModel):
    server: str
    login: str
    password: str
    db_name: str


def load_config(path: str | None = None):
    env = Env()
    env.read_env(path)

    return Config(
        secret_key=env('SECRET_KEY'),
        algorithm=env('ALGORITHM'),
        expire_minutes=env('ACCESS_TOKEN_EXPIRE_MINUTES')
    )


def load_db_config(path: str | None = None):
    env = Env()
    env.read_env(path)

    return DBConfig(
        server=env('DB_SERVER'),
        login=env('DB_LOGIN'),
        password=env('DB_PASSWORD'),
        db_name=env('DB_NAME')
    )
