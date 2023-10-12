from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.item import Item
from app.schemas.item import ItemSchema, ItemResponse


router = APIRouter(prefix='/item')


@router.get('/{item_id}', status_code=status.HTTP_200_OK, response_model=ItemResponse)
async def get_item(item_id: int, db_session: AsyncSession = Depends(get_db)):
    return await Item.get(item_id=item_id, db_session=db_session)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ItemResponse)
async def create_item(payload: ItemSchema, db_session: AsyncSession = Depends(get_db)):
    item = Item(**payload.model_dump())
    await item.save(db_session=db_session)
    return item


@router.patch("/{item_id}", status_code=status.HTTP_202_ACCEPTED, response_model=ItemResponse)
async def update_item(item_id: int, payload: ItemSchema, db_session: AsyncSession = Depends(get_db)):
    item = await Item.get(item_id=item_id, db_session=db_session)
    item.update(**payload.model_dump())
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT, response_model=ItemResponse)
async def delete_item(item_id: int, db_session: AsyncSession = Depends(get_db)):
    item = await Item.get(item_id=item_id, db_session=db_session)
    return await item.delete(db_session=db_session)
