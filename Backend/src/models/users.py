import uuid
from datetime import datetime

# This import is for getting specific datatypes for any specific database.
# Like in below line we are using sqlalchemy.dialect.postgresql for getting access of postgreSQL datatypes.
import sqlalchemy.dialects.postgresql as pg
from sqlmodel import SQLModel, Field,Column

class User(SQLModel, table=True):
    __tablename__ = "Users"
    uid: uuid.UUID = Field(
        sa_column = Column(
            pg.UUID,
            nullable = False,
            primary_key = True,
            default = uuid.uuid4
        )
    )
    username : str
    email : str
    password_hash : str = Field(exclude=True)
    first_name : str
    last_name : str
    is_verified : bool = Field(default=False)
    created_at :datetime = Field(
        sa_column = Column(
            pg.TIMESTAMP,
            default =datetime.now()
        )
    )
    updated_at : datetime = Field(
        sa_column = Column(
            pg.TIMESTAMP,
            default = datetime.now(),
            onupdate = datetime.now()
        )
    )

    def __repr__(self):
        return f"<Users {self.username}>"