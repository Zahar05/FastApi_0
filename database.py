from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, DeclarativeBase

engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)

# async_session = sessionmaker(
#     engine,
#     expire_on_commit=False,
#     class_=AsyncSession
# )
new_session = async_sessionmaker(engine, expire_on_commit=False)


# Base = declarative_base()

class Model(DeclarativeBase):
    pass


class TaskOrm(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[Optional[str]] = mapped_column()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)