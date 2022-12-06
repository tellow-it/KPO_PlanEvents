from datetime import date
from typing import Optional
from sqlalchemy import Enum
from sqlmodel import SQLModel, Field, Relationship


class Sex(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class Person(SQLModel, table=True):
    __tablename__ = "person"

    id: Optional[str] = Field(None, primary_key=True, nullable=False)
    name: str
    birth: date
    sex: Sex
    phone_number: str

    users: Optional["Users"] = Relationship(
        sa_relationship_kwargs={'uselist': False}, back_populates="person")
