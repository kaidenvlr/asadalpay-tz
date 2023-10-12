from fastapi import APIRouter

from app.api.v1.item import router as item_router
from app.api.v1.order import router as order_router

router = APIRouter(prefix='/api/v1')

router.include_router(item_router)
router.include_router(order_router)
