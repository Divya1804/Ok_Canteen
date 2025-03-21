from datetime import timedelta, datetime
from typing import Any

from passlib.context import CryptContext
import jwt
import uuid
from src.config.config_db import Config
import logging

password_context = CryptContext(
    schemes=['bcrypt']
)

def generate_password_hash(password : str) -> str:
    hash = password_context.hash(password)
    return hash

def verify_password(password: str, password_hash: str) -> bool:
    return password_context.verify(password, password_hash)

def create_access_tokens(user_data: dict, refresh: bool = False, expiry: timedelta = None):
    payload = {}
    payload['user'] = user_data
    payload['exp'] = datetime.now() + (expiry if expiry is not None else timedelta(seconds=Config.ACCESS_TOKEN_EXPIRY))
    payload['jti'] = str(uuid.uuid4())
    payload['refresh'] = refresh
    token = jwt.encode(
        payload = payload,
        key = Config.JWT_SECRET_KEY,
        algorithm = Config.JWT_ALGORITHM
    )

    return token

def decode_token(token: str) -> dict | None:
    try:
        token_data = jwt.decode(
            jwt=token,
            key=Config.JWT_SECRET_KEY,
            algorithms=[Config.JWT_ALGORITHM]
        )
        return token_data
    except jwt.PyJWTError as e:
        logging.exception(e)
        return None