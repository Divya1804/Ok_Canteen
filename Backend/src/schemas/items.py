import uuid
from typing import List
from pydantic import BaseModel, Field
from datetime import datetime

class ItemsCreateModel(BaseModel):
    item_name: str = Field(max_length=255)
    description: str = Field(max_length=500, min_length=50)
    price: float
    image_urls: List[str]

class ItemsModel(BaseModel):
    item_name: str = Field(max_length=255)
    description: str = Field(max_length=500, min_length=50)
    price: float = Field(default = 0.0)
    image_urls: List[str]
    category_id: uuid.UUID
    is_available: bool
    created_at: datetime
    updated_at: datetime
