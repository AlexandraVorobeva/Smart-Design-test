from fastapi import APIRouter
from .product import router as product_router

router = APIRouter()
router.include_router(product_router)
