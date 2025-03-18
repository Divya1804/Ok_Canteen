from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from src.config.config_db import Config

engine: AsyncEngine = AsyncEngine(
    create_engine(
        url=Config.DATABASE_URL,
        echo=True
    )
)

async def init_db():
    async  with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session():
    session = sessionmaker(
        bind=engine, expire_on_commit=False, class_=AsyncSession
    )

    async with session() as session:
        yield session