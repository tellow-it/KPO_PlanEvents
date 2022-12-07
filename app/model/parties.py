from typing import Optional
from sqlalchemy import Column, String, Boolean
from sqlmodel import SQLModel, Field


class Party(SQLModel, table=True):
    __tablename__ = "parties"

    id: Optional[str] = Field(None, primary_key=True, nullable=False)
    name: str = Field(sa_column=Column("name", String), nullable=False)
    description: Optional[str] = Field(sa_column=Column("description", String))
    admin_id: str = Field(sa_column=Column('admin_id', String))
    lock_bucket: Optional[bool] = Field(sa_column=Column('lock_basket', Boolean), default=False)
