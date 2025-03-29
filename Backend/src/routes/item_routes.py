from src.db.main import get_session
from src.schemas.items import ItemsCreateModel
from src.services.items_service import ItemsService
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

items_router = APIRouter()
items_service = ItemsService()

@items_router.get('/{category_name}/items/')
async def get_all_items(category_name: str, session: AsyncSession = Depends(get_session)):
    data = await items_service.get_all_items_by_category(category_name, session)
    return data

@items_router.post('/{category_name}/items/')
async def create_new_item(category_name: str, item_data: ItemsCreateModel, session: AsyncSession = Depends(get_session)):
    data = await items_service.create_new_item(category_name, item_data, session)
    return data

# @items_router.get()