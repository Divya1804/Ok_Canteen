from pydantic import BaseModel, Field

class ReviewsCreateModel(BaseModel):
    comment: str = Field(max_length=200)
    rating: int = Field(ge=1, le=5)
