import uuid
from datetime import datetime

import sqlalchemy.dialects.postgresql as pg
from sqlmodel import SQLModel, Field, Column


class Category(SQLModel, table=True):
    __tablename__ = "categories"

    category_id: uuid.UUID = Field(
        sa_column = Column(
            pg.UUID,
            nullable = False,
            primary_key = True,
            default = uuid.uuid4
        )
    )
    category_name: str = Field(
        sa_column = Column(
            pg.VARCHAR(255),
            unique = True,
            nullable = False
        )
    )
    description: str | None = Field(
        sa_column = Column(
            pg.TEXT,
            unique = True,
            nullable = True
        )
    )
    created_at: datetime = Field(
        sa_column = Column(
            pg.TIMESTAMP,
            default = datetime.now()
        )
    )
    updated_at: datetime = Field(
        sa_column = Column(
            pg.TIMESTAMP,
            default = datetime.now(),
            onupdate = datetime.now()
        )
    )

    def __repr__(self):
        return f"<Users {self.category_name}>"