from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    phone: Optional[str]
    password: str
    is_staff: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                "username": "ivan",
                "email": "mr.test@gmail.com",
                "phone": '88005553555',
                "password": "admin",
                "is_staff": False
            }
        }


class Settings(BaseModel):
    authjwt_secret_key: str = '38d34af6ebad88dc4a53ea7e792f8d2f937d660102f97e9d7cfb9a1a68889afe'


class LoginModel(BaseModel):
    username: str
    password: str
