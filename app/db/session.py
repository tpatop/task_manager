from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)

from core.config import load_db_config, DBConfig
from .models import Base

config: DBConfig = load_db_config()

url = f"postgresql+asyncpg://{config.login}:{config.password}@localhost/{config.name_db}"
async_engine = create_async_engine(url, echo=False, pool_pre_ping=True)

async_session = async_sessionmaker(
    async_engine, autocommit=False, expire_on_commit=False,
    class_=AsyncSession, autoflush=False
)


async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def close_db():
    await async_engine.dispose()


async def get_session():
    async with async_session() as session:
        yield session