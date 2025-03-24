from typing import List
from src.models.users import User
from fastapi.exceptions import HTTPException
from fastapi import status, Request, Depends
from fastapi.security.http import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from src.utils.user_utils import decode_token
from src.db.redis import jti_in_blocklist
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from src.services.user_auth_service import UserService

user_service = UserService()


class TokenBearer(HTTPBearer):
    def __init__(self, auto_error=True):
        super().__init__(auto_error=auto_error)
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None :
        creds = await super().__call__(request)

        token = creds.credentials
        token_data = decode_token(token)
        if not self.token_valid(token):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="INVALID or EXPIRED Token.")

        if await jti_in_blocklist(token_data['jti']):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={
                "error" : "This token is expired or revoked.",
                "hint":"Please get a new token."
            })

        self.verify_token(token_data)
        return token_data

    def token_valid(self, token: str) -> bool:
        token_data = decode_token(token)
        return True if token_data is not None else False

    def verify_token(self, token_data: dict):
        raise NotImplementedError("Please Override this method in child classes")


class AccessTokenBearer(TokenBearer):
    def verify_token(self, token_data: dict) -> None:
        if token_data and token_data['refresh']:
            raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail="Please provide an access token.")


class RefreshTokenBearer(TokenBearer):
    def verify_token(self, token_data: dict) -> None:
        if token_data and not token_data['refresh']:
            raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail="Please provide a refresh token.")


async def get_current_user(token_details: dict = Depends(AccessTokenBearer()), session: AsyncSession = Depends(get_session)):
    user_email = token_details['user']['email']
    print(user_email)
    user = await user_service.get_user_by_email(user_email, session)
    return user


class RoleChecker:
    def __init__(self, allowed_roles: List[str]) -> None:
        self.allowed_roles = allowed_roles

    def __call__(self, current_user: User = Depends(get_current_user)):
        if current_user.role in self.allowed_roles:
            return True
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail={
            "Error" : "You are not authorizes person for this operation."
        })
