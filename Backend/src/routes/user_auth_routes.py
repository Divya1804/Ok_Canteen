from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from src.schemas.users import UserCreateModel, UserModel
from src.services.user_auth_service import UserService
from src.db.main import get_session

auth_router = APIRouter()
user_service = UserService()

@auth_router.post('/signup', response_model=UserModel, status_code=status.HTTP_201_CREATED, description="New user is created")
async def create_user_account(user_data: UserCreateModel,session: AsyncSession = Depends(get_session)):
    email = user_data.email
    user_exists = await user_service.user_exists(email, session)
    if user_exists:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User with this email already exists...")
    new_user = await user_service.create_user_acc(user_data, session)
    return new_user