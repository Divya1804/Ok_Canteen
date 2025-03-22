from fastapi.exceptions import HTTPException
from fastapi import status
from urllib.request import Request
from fastapi.security.http import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from src.utils.user_utils import decode_token

class AccessTokenBearer(HTTPBearer):
    def __init__(self, auto_error=True):
        super().__init__(auto_error=auto_error)
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None :
        creds = await super().__call__(request)

        # print(creds)
        # print()
        # print(creds.scheme)

        token = creds.credentials
        token_data = decode_token(token)
        if not self.token_valid:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="INVALID or EXPIRED Token.")

        if token_data['refresh']:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Please provide an access token.")
        
        return creds

    def token_valid(self, token: str) -> bool:
        token_data = decode_token(token)
        return True if token_data is not None else False