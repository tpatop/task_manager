from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)

from src.core.config import load_db_config, DBConfig


cfg: DBConfig = load_db_config()

url = f"postgresql+asyncpg://{cfg.login}:{cfg.password}@{cfg.server}/{cfg.db_name}"
async_engine = create_async_engine(url, echo=False, pool_pre_ping=True)

async_session = async_sessionmaker(
    async_engine, autocommit=False, expire_on_commit=False,
    class_=AsyncSession, autoflush=False
)


async def get_session():
    async with async_session() as session:
        yield session
