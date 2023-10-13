from sqlalchemy import Integer, String, ForeignKey, select, Boolean
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.exceptions import NotFoundException
from app.models.base import Base


class OrderItem(Base):
    __tablename__ = "order_item"
    __table_args__ = ({"schema": "app"},)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("app.item.id"), nullable=False)
    order_id: Mapped[int] = mapped_column(ForeignKey("app.order.id"), nullable=True)
    quantity: Mapped[int] = mapped_column(Integer, default=1)

    order = relationship("Order", back_populates="order_items", lazy="selectin")
    item = relationship("Item", back_populates="order_items", lazy="selectin")


class Order(Base):
    __tablename__ = "order"
    __table_args__ = ({"schema": "app"},)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    telegram_id: Mapped[str] = mapped_column(String)
    status: Mapped[bool] = mapped_column(Boolean, default=False)
    uuid_asadal: Mapped[str] = mapped_column(String, nullable=True)

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

    @classmethod
    async def get_all(cls, telegram_id: str, db_session: AsyncSession):
        stmt = select(cls).where(cls.telegram_id == telegram_id)
        result = await db_session.execute(stmt)
        instance = result.scalars().all()
        return instance
