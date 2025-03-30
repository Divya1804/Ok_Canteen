import uuid
from datetime import datetime
from typing import Literal, List, Optional
from pydantic import BaseModel, Field

class FixedDishCreateModel(BaseModel):
    day_of_week: Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    sabji_name: str = Field(max_length=50)
    image_urls: List[str]
    roti_count: int = Field(default = 3, ge=3)
    price: float = Field(default=0.0)
    created_at: Optional[datetime] = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=datetime.now())

class FixedDishModel(BaseModel):
    fixed_dish_id: uuid.UUID
    day_of_week: Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    sabji_name: str = Field(max_length=50)
    image_urls: List[str]
    roti_count: int = Field(default=3, ge=3)
    price: float = Field(default=0.0)
    is_available: bool
    created_at: datetime
    updated_at: datetime

class FixedDishUpdateModel(BaseModel):
    day_of_week: Optional[Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]] = Field(default=None)
    sabji_name: Optional[str] = Field(max_length=50, default=None)
    image_urls: Optional[List[str]] = Field(default_factory=[])
    roti_count: Optional[int] = Field(default=3, ge=3)
    price: Optional[float] = Field(default=0.0)
    is_available: Optional[bool] = Field(default=True)
    updated_at: Optional[datetime] = Field(default= datetime.now())