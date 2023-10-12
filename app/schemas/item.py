from pydantic import BaseModel, Field


class ItemSchema(BaseModel):
    title: str = Field(title="", description="")
    price: float = Field(title="", description="")


class ItemResponse(BaseModel):
    id: int = Field(title="", description="")
    title: str = Field(title="", description="")
    price: float = Field(title="", description="")
