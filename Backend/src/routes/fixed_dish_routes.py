from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import JSONResponse
from src.services.fixed_dish_service import FixedDishService
from src.schemas.fixed_dish import FixedDishModel, FixedDishUpdateModel, FixedDishCreateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from src.utils.dependencies import AccessTokenBearer, RoleChecker

fixed_dish_router = APIRouter()
fixed_dish_service = FixedDishService()
access_token_bearer = AccessTokenBearer()
admin_role_check = Depends(RoleChecker(['ADMIN']))
user_role_check = Depends(RoleChecker(['ADMIN', 'USER']))

@fixed_dish_router.get('/')
async def get_all_data(session: AsyncSession = Depends(get_session)):
    data = await fixed_dish_service.get_all_fixed_dish_data(session)
    return data

@fixed_dish_router.get('/{day_of_week}')
async def get_data_by_day(day_of_week: str, session: AsyncSession = Depends(get_session)):
    data = await fixed_dish_service.get_fixed_dish_by_day(day_of_week, session)

    if not data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Fixed dish not found for today...")
    return data

@fixed_dish_router.post('/')
async def create_fixed_dish(fixed_dish_data: FixedDishCreateModel, session: AsyncSession = Depends(get_session)):
    print(fixed_dish_data)
    data = await fixed_dish_service.create_fixed_dish_data(fixed_dish_data, session)
    print(f"\n\n{data}\n\n")
    return data

@fixed_dish_router.put('/{day_of_week}')
async def update_fixed_dish_data(day_of_week: str, fixed_dish_data: FixedDishUpdateModel, session: AsyncSession = Depends(get_session)):
    data = await fixed_dish_service.update_fixed_dish_data(day_of_week, fixed_dish_data, session)
    return data

@fixed_dish_router.delete('/{day_of_week}')
async def delete_fixed_dish_data(day_of_week: str, session: AsyncSession = Depends(get_session)):
    await fixed_dish_service.delete_fixed_dish(day_of_week, session)
    return JSONResponse(
        content={
            "Message" : "Fixed dish data deleted..."
        }
    )