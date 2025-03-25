from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import JSONResponse
from src.services.category_service import CategoryService
from src.schemas.categories import CategoryCreateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session

category_router = APIRouter()
category_service = CategoryService()

@category_router.get('/')
async def get_all_categories(session: AsyncSession = Depends(get_session)):
    all_categories = await category_service.get_all_categories(session)
    return all_categories

@category_router.get('/{category_name}')
async def get_category_by_name(category_name: str, session: AsyncSession = Depends(get_session)):
    category_data = await category_service.get_category_details(category_name, session)

    if not category_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category data not found")

    return category_data

@category_router.post('/')
async def create_category(category_data: CategoryCreateModel, session: AsyncSession = Depends(get_session)):
    category = await category_service.create_category(category_data, session)

    if not category:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail="Category not created properly")

    return category

@category_router.put('/{category_name}')
async def update_category_data(category_name: str, category_data: CategoryCreateModel, session: AsyncSession = Depends(get_session)):
    updated_category = await category_service.update_category_data(category_name, category_data, session)

    if not updated_category:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Category data is not updated properly.")

    return updated_category

@category_router.delete('/{category_name')
async def delete_category(category_name: str, session: AsyncSession = Depends(get_session)):
    await category_service.delete_category(category_name, session)
    return JSONResponse(
        content={
            "message" : "Category has been deleted properly."
        }
    )