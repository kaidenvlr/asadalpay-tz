from typing import Any

from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase, declared_attr, declarative_base

Base = declarative_base()


# class Base(Base_):
#     id: Any
#     __name__: str
#
#     @declared_attr
#     def __tablename__(self) -> str:
#         return self.__name__.lower()
#
#     async def save(self, db_session: AsyncSession):
#         try:
#             db_session.add(self)
#             await db_session.commit()
#         except SQLAlchemyError as ex:
#             raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=repr(ex)) from ex
#
#     async def delete(self, db_session: AsyncSession):
#         try:
#             await db_session.delete(self)
#             await db_session.commit()
#             return True
#         except SQLAlchemyError as ex:
#             raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=repr(ex)) from ex
#
#     async def update(self, db_session: AsyncSession, **kwargs):
#         try:
#             for k, v in kwargs.items():
#                 setattr(self, k, v)
#             return await db_session.commit()
#         except SQLAlchemyError as ex:
#             raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=repr(ex)) from ex
