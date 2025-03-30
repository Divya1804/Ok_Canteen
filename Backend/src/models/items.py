import uuid
from datetime import datetime
from sqlalchemy import ForeignKey
from typing import List
import sqlalchemy.dialects.postgresql as pg
from sqlmodel import SQLModel, Field, Column

class Items(SQLModel, table=True):
    __tablename__ = "items"
    item_id: uuid.UUID = Field(sa_column= Column(
        pg.UUID, nullable= False, default= uuid.uuid4, primary_key= True
    ))
    category_id : uuid.UUID = Field(sa_column= Column(
        pg.UUID, ForeignKey("categories.category_id"), nullable= False
    ))
    item_name : str = Field(sa_column=Column(
        pg.VARCHAR(255), unique=True, nullable=False
    ))
    description: str | None = Field(sa_column=Column(
        pg.TEXT, nullable=True
    ))
    price: float = Field(sa_column=Column(
        pg.FLOAT,
        nullable=False
    ))
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