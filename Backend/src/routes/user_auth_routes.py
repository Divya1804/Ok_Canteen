from datetime import timedelta, datetime
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from src.schemas.users import UserCreateModel, UserModel, UserLoginModel
from src.services.user_auth_service import UserService
from src.db.main import get_session
from src.utils.user_utils import create_access_tokens, decode_token, verify_password
from fastapi.responses import JSONResponse
from src.utils.dependencies import RefreshTokenBearer

REFRESH_TOKEN_EXPIRY = 2

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

@auth_router.get("/refresh")
async def get_new_access_token(token_details: dict = Depends(RefreshTokenBearer())):
    print(token_details)
    print()
    expiry_timestamp = token_details["exp"]

    if datetime.fromtimestamp(expiry_timestamp) > datetime.now():
        new_access_token = create_access_tokens(user_data=token_details["user"])

        return JSONResponse(content={"access_token": new_access_token})



@auth_router.post('/login')
async def login_users(login_data: UserLoginModel, session: AsyncSession = Depends(get_session)):
    email = login_data.email
    password = login_data.password_hash

    user = await user_service.get_user_by_email(email, session)

    if user is not None:
        valid_password = verify_password(password, user.password_hash)
        if valid_password:
            access_token = create_access_tokens(user_data={
                'email': user.email,
                'user_uid': str(user.uid)
            })

            refresh_token = create_access_tokens(user_data={
                    'email': user.email,
                    'user_uid': str(user.uid)
                },
                refresh=True,
                expiry=timedelta(days = REFRESH_TOKEN_EXPIRY)
            )

            return JSONResponse(
                content={
                    "Message" : "Login Successful",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "user": {
                        "email": user.email,
                        "uid": str(user.uid)
                    }

                }
            )

    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is not authenticated.")