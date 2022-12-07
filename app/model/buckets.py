from typing import List, Optional
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import relationship


class Bucket(SQLModel, table=True):
    __tablename__ = "buckets"

    id: Optional[str] = Field(None, primary_key=True, nullable=False)
    name: str = Field(sa_column=Column("name", String), nullable=False)
    quantity: int = Field(sa_column=Column("quantity", Integer))
    price: int = Field(sa_column=Column('price', Integer))

    party_id = Column(String, ForeignKey("parties.id"))
    party = relationship('Party', back_populates='buckets')
