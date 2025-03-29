from src.models.categories import Category
from src.models.items import Items
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from fastapi import status
from fastapi.exceptions import HTTPException
from src.schemas.items import ItemsCreateModel, ItemUpdateModel
from src.services.category_service import CategoryService

category_service = CategoryService()

class ItemsService:
    async def get_all_items_by_category(self, category_name: str, session: AsyncSession):
        category_data = await category_service.get_category_details(category_name, session)
        if category_data is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found...")

        statement = select(Items).join(Category).where(category_name == Category.category_name)
        result = await session.exec(statement)
        return result.all()

    async def get_items_data(self, category_name: str, item_name: str, session: AsyncSession):
        category_data = await category_service.get_category_details(category_name, session)
        if category_data is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found...")

        statement = select(Items).where(Items.item_name == item_name)
        result = await session.exec(statement)
        return result.first()

    async def create_new_item(self, category_name: str, item_data: ItemsCreateModel, session: AsyncSession):
        category_data = await category_service.get_category_details(category_name, session)
        if category_data is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found...")

        item_data_dict = item_data.model_dump()
        new_item_data = Items(
            **item_data_dict
        )
        new_item_data.category_id = category_data.category_id
        session.add(new_item_data)
        await session.commit()
        return new_item_data

    async def update_item_data(self, category_name: str, item_name: str, item_data: ItemUpdateModel, session: AsyncSession):
        statement = select(Category).where(Category.category_name == category_name)
        result = await session.exec(statement)
        if result.first() is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category name not present...")

        item = await self.get_items_data(category_name, item_name, session)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

        for key, value in item_data.model_dump(exclude_unset=True).items():
            setattr(item, key, value)

        session.add(item)
        await session.commit()
        await session.refresh(item)
        return item

    async def delete_item_data(self, category_name:str, item_name: str, session: AsyncSession):
        statement = select(Category).where(Category.category_name == category_name)
        result = await session.exec(statement)
        if result.first() is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category name not present...")

        item = await self.get_items_data(category_name, item_name, session)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

        await session.delete(item)
        await session.commit()
        return None
