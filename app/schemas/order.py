from pydantic import BaseModel, Field


class OrderItemSchema(BaseModel):
    item_id: int = Field(title="", description="")
    quantity: int = Field(title="", description="")


class OrderSchema(BaseModel):
    telegram_id: str = Field(title="", description="")
    order_items: list[OrderItemSchema] = Field(title="", description="")


class OrderResponse(BaseModel):
    id: int = Field(title="", description="")
    telegram_id: str = Field(title="", description="")
    order_items: list[OrderItemSchema] = Field(title="", description="")
