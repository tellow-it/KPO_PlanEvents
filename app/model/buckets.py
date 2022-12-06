from typing import List, Optional
from sqlalchemy import Column, String, Integer
from sqlmodel import SQLModel, Field, Relationship


class Bucket(SQLModel, table=True):
    __tablename__ = "buckets"

    id: Optional[str] = Field(None, primary_key=True, nullable=False)
    name: str = Field(sa_column=Column("name", String), nullable=False)
    quantity: Optional[str] = Field(sa_column=Column("quantity", String))
    price: str = Field(sa_column=Column('price', Integer))
