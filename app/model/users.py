from typing import List, Optional
from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field, Relationship


class Users(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[str] = Field(None, primary_key=True, nullable=False)
    username: str = Field(sa_column=Column("username", String, unique=True))
    email: str = Field(sa_column=Column("email", String, unique=True))
    password: str

    person_id: Optional[str] = Field(default=None, foreign_key="person.id")
    person: Optional["Person"] = Relationship(back_populates="users")
