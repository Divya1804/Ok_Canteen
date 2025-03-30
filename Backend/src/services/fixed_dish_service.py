from src.models.fixed_dish import Fixed_dish
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from fastapi import status
from fastapi.exceptions import HTTPException
from src.schemas.fixed_dish import FixedDishModel, FixedDishCreateModel, FixedDishUpdateModel

class FixedDishService:
    async def get_all_fixed_dish_data(self, session: AsyncSession):
        statement = select(Fixed_dish).order_by(Fixed_dish.day_of_week)
        result = await session.exec(statement)
        print(f"\n\n{result}\n\n")
        return result.all()

    async def get_fixed_dish_by_day(self, day_of_week: str, session: AsyncSession):
        statement = select(Fixed_dish).where(Fixed_dish.day_of_week == day_of_week)
        print(f"\n\n{statement}\n\n")
        result = await session.exec(statement)

        return result.first()

    async def create_fixed_dish_data(self, fixed_dish_data: FixedDishCreateModel, session: AsyncSession):
        fixed_dish_data_dict = fixed_dish_data.model_dump()
        new_fixed_dish_data = Fixed_dish(**fixed_dish_data_dict)

        session.add(new_fixed_dish_data)
        await session.commit()
        return new_fixed_dish_data

    async def update_fixed_dish_data(self, day_of_week: str, fixed_dish_data: FixedDishUpdateModel, session: AsyncSession):
        old_data = await self.get_fixed_dish_by_day(day_of_week, session)
        if not old_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found for given day...")

        for key, value in fixed_dish_data.model_dump(exclude_unset=True).items():
            setattr(old_data, key, value)

        session.add(old_data)
        await session.commit()
        await session.refresh(old_data)
        return old_data

    async def delete_fixed_dish(self, day_of_week: str, session: AsyncSession):
        old_data = await self.get_fixed_dish_by_day(day_of_week, session)
        if not old_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found for given day...")

        await session.delete(old_data)
        await session.commit()
        return None