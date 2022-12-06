from fastapi import HTTPException
import logging
import re
from typing import TypeVar, Optional

from pydantic import BaseModel, validator
from app.model.person import Sex

T = TypeVar('T')

# get root logger
logger = logging.getLogger(__name__)


class RegisterSchema(BaseModel):
    username: str
    email: str
    name: str
    password: str
    phone_number: str
    birth: str
    sex: Sex

    # phone number validation

    @validator("phone_number")
    def phone_validation(cls, number):
        logger.debug(f"phone in 2 validatior: {number}")
        if len(number) > 12:
            raise HTTPException(status_code=400, detail="Invalid input phone number!")
        return number

    # Sex validation
    @validator("sex")
    def sex_validation(cls, sex_status):
        if hasattr(Sex, sex_status) is False:
            raise HTTPException(status_code=400, detail="Invalid input sex")
        return sex_status


class LoginSchema(BaseModel):
    username: str
    password: str


class User_s_PartySchema(BaseModel):
    id: str


class CreatePartySchema(BaseModel):
    name: str
    description: Optional[str]
    admin_id: str
    lock_bucket: Optional[bool]


class ReadPartySchema(BaseModel):
    id: str


class UpdatePartySchema(BaseModel):
    id: str
    name: Optional[str]
    description: Optional[str]
    admin_id: Optional[str]
    lock_bucket: Optional[bool]


class DeletePartySchema(BaseModel):
    id: str


class CreateBucketSchema(BaseModel):
    name: str
    quantity: str
    price: str


class ReadBucketSchema(BaseModel):
    id: str


class UpdateBucketSchema(BaseModel):
    id: str
    name: Optional[str]
    quantity: Optional[str]
    price: Optional[str]


class DeleteBucketSchema(BaseModel):
    id: str


class ForgotPasswordSchema(BaseModel):
    email: str
    new_password: str


class DetailSchema(BaseModel):
    status: str
    message: str
    result: Optional[T] = None


class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None
