from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field


class M2M_User_Party(SQLModel, table=True):
    __tablename__ = "m2m_user_party"

    user_id: str = Field(sa_column=Column('user_id', String))
    party_id: str = Field(sa_column=Column('party_id', String))
