import uuid
from datetime import datetime
from typing import List
import sqlalchemy.dialects.postgresql as pg
from sqlmodel import SQLModel, Field ,Column

class Fixed_dish(SQLModel, table=True):
    __tablename__ = "fixed_dish"

    fixed_dish_id: uuid.UUID = Field(sa_column=Column(
        pg.UUID,
        nullable=False,
        default=uuid.uuid4,
        primary_key=True
    ))

    day_of_week: str = Field(sa_column=Column(
        pg.VARCHAR(255),
        nullable=False,
        unique=True
    ), max_length=10)

    sabji_name: str = Field(sa_column=Column(
        pg.VARCHAR(255),
        nullable=False
    ), max_length=50)

    roti_count: int = Field(nullable=False, default = 3)

    price: float = Field(nullable=False)

    is_available: bool = Field(sa_column=Column(
        pg.BOOLEAN, nullable=False, default=True
    ))

    # ✅ Store multiple images as JSON array
    image_urls: List[str] = Field(
        sa_column=Column(pg.JSON, nullable=True, default=[])
    )

    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP, default=datetime.now
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP, default=datetime.now, onupdate=datetime.now
        )
    )

    def __repr__(self):
        return f"<{self.day_of_week}'s Fixed_dish = {self.sabji_name}>"