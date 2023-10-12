from fastapi import APIRouter, Depends, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.exceptions import NonProcessableEntityException
from app.models.item import Item
from app.schemas.item import ItemSchema, ItemResponse


router = APIRouter(prefix='/item')


@router.get('/{item_id}', status_code=status.HTTP_200_OK, response_model=ItemResponse)
async def get_item(item_id: int, db_session: AsyncSession = Depends(get_db)):
    return await Item.get(item_id=item_id, db_session=db_session)


@router.get('', status_code=status.HTTP_200_OK, response_model=list[ItemResponse])
async def get_items(db_session: AsyncSession = Depends(get_db)):
    return await Item.get_all(db_session=db_session)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ItemResponse)
async def create_item(payload: ItemSchema, db_session: AsyncSession = Depends(get_db)):
    item = Item(**payload.model_dump())
    try:
        db_session.add(item)
        await db_session.commit()
    except SQLAlchemyError as ex:
        raise NonProcessableEntityException(msg=repr(ex))
    return item


@router.patch("/{item_id}", status_code=status.HTTP_202_ACCEPTED, response_model=ItemResponse)
async def update_item(item_id: int, payload: ItemSchema, db_session: AsyncSession = Depends(get_db)):
    item = await Item.get(item_id=item_id, db_session=db_session)
    try:
        for k, v in payload.items():
            setattr(item, k, v)
        await db_session.commit()
    except SQLAlchemyError as ex:
        raise NonProcessableEntityException(msg=repr(ex))
    return item


@router.delete("/{item_id}", response_model=ItemResponse)
async def delete_item(item_id: int, db_session: AsyncSession = Depends(get_db)):
    item = await Item.get(item_id=item_id, db_session=db_session)
    try:
        await db_session.delete(item)
        await db_session.commit()
        return True
    except SQLAlchemyError as ex:
        raise NonProcessableEntityException(msg=repr(ex))
