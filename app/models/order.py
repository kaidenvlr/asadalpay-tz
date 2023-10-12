from sqlalchemy import Integer, String, ForeignKey, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.exceptions import NotFoundException
from app.models.base import Base


class Order(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    telegram_id: Mapped[str] = mapped_column(String)

    order_items = relationship("OrderItem", back_populates="order")

    @classmethod
    async def get(cls, order_id: int, db_session: AsyncSession):
        stmt = select(cls).where(cls.id == order_id)
        result = await db_session.execute(stmt)
        instance = result.scalars().first()
        if instance is None:
            raise NotFoundException(msg="Order not found")
        else:
            return instance


class OrderItem(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("app.item.id"), nullable=False)
    order_id: Mapped[int] = mapped_column(ForeignKey("app.order.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, default=1)

    order = relationship("Order", back_populates="order_items")
    item = relationship("Item", back_populates="order_items")
