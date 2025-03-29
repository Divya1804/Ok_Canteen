from typing import List
from src.db.main import get_session
from src.schemas.items import ItemsCreateModel, ItemUpdateModel, ItemsModel
from src.services.items_service import ItemsService
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel.ext.asyncio.session import AsyncSession
from src.utils.dependencies import RoleChecker, AccessTokenBearer

items_router = APIRouter()
items_service = ItemsService()
access_token_bearer = AccessTokenBearer()
admin_role_check = Depends(RoleChecker(['ADMIN']))
user_role_check = Depends(RoleChecker(['ADMIN', 'USER']))

@items_router.get('/{category_name}/items/', response_model=List[ItemsModel], dependencies=[user_role_check])
async def get_all_items(category_name: str, session: AsyncSession = Depends(get_session), _:dict = Depends(access_token_bearer)):
    data = await items_service.get_all_items_by_category(category_name, session)
    return data

@items_router.post('/{category_name}/items/', dependencies=[admin_role_check])
async def create_new_item(category_name: str, item_data: ItemsCreateModel, session: AsyncSession = Depends(get_session), _:dict = Depends(access_token_bearer)):
    data = await items_service.create_new_item(category_name, item_data, session)
    return data

@items_router.get("/{category_name}/items/{item_name}", dependencies=[user_role_check])
async def get_item_data(category_name: str, item_name: str, session: AsyncSession = Depends(get_session), _:dict = Depends(access_token_bearer)):
    data = await items_service.get_items_data(category_name, item_name, session)
    return data

@items_router.put("/{category_name}/items/{item_name}", dependencies=[admin_role_check])
async def update_item_data(category_name: str, item_name: str, item_data: ItemUpdateModel, session: AsyncSession = Depends(get_session), _:dict = Depends(access_token_bearer)):
    data = await items_service.update_item_data(category_name, item_name, item_data, session)
    return data

@items_router.delete('/{category_name}/items/{item_name}', dependencies=[admin_role_check])
async def delete_item_data(category_name: str, item_name: str, session: AsyncSession = Depends(get_session), _:dict = Depends(access_token_bearer)):
    await items_service.delete_item_data(category_name, item_name, session)
    return JSONResponse(
        content = {
            "message" : "Item has been deleted properly."
        }
    )
