from src.models.categories import Category
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from fastapi import status
from fastapi.exceptions import HTTPException
from src.schemas.categories import CategoryModel, CategoryCreateModel

class CategoryService:
    async def get_category_details(self, category_name: str, session: AsyncSession):
        statement = select(Category).where(Category.category_name == category_name)
        result = await session.exec(statement)
        category_data = result.first()
        return category_data

    async def get_all_categories(self, session: AsyncSession):
        statement = select(Category)
        result = await session.exec(statement)
        return result.all()

    async def category_exist(self, category_name: str, session: AsyncSession):
        category = await self.get_category_details(category_name, session)
        return True if category is not None else False

    async def create_category(self, category_data: CategoryCreateModel, session: AsyncSession):
        category_data_dict = category_data.model_dump()
        new_category = Category(**category_data_dict)

        check_category = await self.category_exist(category_data.category_name, session)
        if check_category:
            raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail="Category already exist...")

        session.add(new_category)
        await session.commit()
        return new_category

    async def update_category_data(self, category_name: str, new_category_data: CategoryCreateModel, session: AsyncSession):
        old_category_data = await self.get_category_details(category_name, session)
        if not old_category_data:
            return None

        for key, value in new_category_data.model_dump(exclude_unset=True).items():
            setattr(old_category_data, key, value)

        session.add(old_category_data)
        await session.commit()
        await session.refresh(old_category_data)
        return old_category_data

    async def delete_category(self, category_name: str, session: AsyncSession) -> None:
        category = await self.get_category_details(category_name, session)
        if not category:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No category found")

        await session.delete(category)
        await session.commit()
        return None