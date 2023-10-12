from sqlalchemy import Integer, String, Float, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.exceptions import NotFoundException
from app.models.base import Base


class Item(Base):
    __tablename__ = "item"
    __table_args__ = ({"schema": "app"},)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)

    order_items = relationship("OrderItem", back_populates="item")

    @classmethod
    async def get(cls, db_session: AsyncSession, item_id: int):
        stmt = select(cls).where(cls.id == item_id)
        result = await db_session.execute(stmt)
        instance = result.scalars().first()
        if instance is None:
            raise NotFoundException(msg="Item not Found")
        else:
            return instance

    @classmethod
    async def get_all(cls, db_session: AsyncSession):
        stmt = select(cls)
        result = await db_session.execute(stmt)
        instance = result.scalars().all()
        return instance
