from typing import Optional
from sqlalchemy import Column, String, Integer
from sqlmodel import SQLModel, Field


class Bucket(SQLModel, table=True):
    __tablename__ = "buckets"

    id: Optional[str] = Field(None, primary_key=True, nullable=False)
    name: str = Field(sa_column=Column("name", String), nullable=False)
    quantity: int = Field(sa_column=Column("quantity", Integer))
    price: int = Field(sa_column=Column('price', Integer))

    party_id: str = Field(sa_column=Column('party_id', String))
