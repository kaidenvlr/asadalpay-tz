from pydantic import BaseModel, Field


class OrderItemSchema(BaseModel):
    item_id: int = Field(title="", description="")
    quantity: int = Field(title="", description="")


class OrderSchema(BaseModel):
    telegram_id: str = Field(title="", description="")
    order_items: list[OrderItemSchema] = Field(title="", description="")
    status: bool = Field(title="", description="")


class OrderResponse(BaseModel):
    id: int = Field(title="", description="")
    url: str = Field(title="", description="")
    full_value: float = Field(title="", description="")


class OrderNativeResponse(BaseModel):
    id: int = Field(title="", description="")
    telegram_id: str = Field(title="", description="")
    status: bool = Field(title="", description="")
