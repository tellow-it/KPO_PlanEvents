from database import Base
from sqlalchemy import Column, Integer, Boolean, Text, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(35), unique=True)
    phone = Column(String(12))
    password = Column(Text)
    is_staff = Column(Boolean, default=False)
    parties = relationship('Party', back_populates='user')

    def __repr__(self):
        return f"<User {self.username}>"


class Party(Base):
    __tablename__ = 'party'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), unique=True)
    creater = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='parties')

    def __repr__(self):
        return f'<Party> {self.id}'
