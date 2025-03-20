from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class UserCreateModel(BaseModel):
    username: str = Field(max_length=20)
    email: str = Field(
        max_length=50,
        pattern=r'^[a-zA-Z0-9_.+-]+@ddu.ac.in+$'
    )
    password_hash: str = Field(min_length=6)
    first_name: str
    last_name: str

class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    password_hash: str = Field(exclude=True)
    first_name: str
    last_name: str
    is_verified: bool
    created_at: datetime
    updated_at: datetime