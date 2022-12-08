from typing import Optional

from sqlalchemy import Column, String, Integer
from sqlmodel import SQLModel, Field


class M2M_User_Party(SQLModel, table=True):
    __tablename__ = "m2m_user_party"

    id: Optional[str] = Field(None, primary_key=True, nullable=False)
    user_id: str = Field(sa_column=Column('user_id', String))
    party_id: str = Field(sa_column=Column('party_id', String))
