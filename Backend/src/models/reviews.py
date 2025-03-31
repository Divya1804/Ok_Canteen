import uuid
from datetime import datetime
from sqlalchemy import ForeignKey
import sqlalchemy.dialects.postgresql as pg
from sqlmodel import SQLModel, Field, Column

class Reviews(SQLModel, table=True):
    __tablename__ = "reviews"
    review_id: uuid.UUID = Field(sa_column=Column(
        pg.UUID, nullable=False, default=uuid.uuid4, primary_key=True
    ))

    user_id: uuid.UUID = Field(sa_column=Column(
        pg.UUID, ForeignKey("Users.uid"), nullable=False
    ))

    item_id: uuid.UUID = Field(sa_column=Column(
        pg.UUID, ForeignKey("items.item_id"), nullable=False
    ))

    comment: str = Field(sa_column=Column(
        pg.TEXT, nullable=True,
    ))

    rating: int = Field(sa_column=Column(
        pg.INTEGER, nullable=False
    ))

    created_at: datetime = Field(sa_column=Column(
        pg.TIMESTAMP, default=datetime.now
    ))

    updated_at: datetime = Field(sa_column=Column(
        pg.TIMESTAMP, default=datetime.now, onupdate=datetime.now
    ))

    def __repr__(self):
        return f"<Review {self.rating}>"