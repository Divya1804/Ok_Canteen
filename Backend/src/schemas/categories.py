from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class CategoryCreateModel(BaseModel):
    category_name: str = Field(max_length = 20)
    description: str = Field(min_length=100)

class CategoryModel(BaseModel):
    category_id: uuid.UUID
    category_name: str = Field(max_length=20)
    description: str = Field(min_length=100)
    created_at: datetime
    updated_at: datetime