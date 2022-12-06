import base64
from datetime import datetime
from uuid import uuid4
from fastapi import HTTPException

from passlib.context import CryptContext

from app.model import Person, Users
from app.schema import RegisterSchema
from app.repository.users import UsersRepository
from app.repository.person import PersonRepository
from app.schema import LoginSchema, ForgotPasswordSchema
from app.repository.auth_repo import JWTRepo


class BucketService:

    @staticmethod
    async def register_service(register: RegisterSchema):

        # Create uuid
        _person_id = str(uuid4())
        _users_id = str(uuid4())

        # convert birth date type from frontend str to date
        birth_date = datetime.strptime(register.birth, '%d-%m-%Y')

        # mapping request data to class entity table
        _person = Person(id=_person_id, name=register.username, birth=birth_date,
                         sex=register.sex, phone_number=register.phone_number)

        _users = Users(id=_users_id, username=register.username, email=register.email,
                       password=pwd_context.hash(register.password),
                       person_id=_person_id)

        # Cheking the same username
        _username = await UsersRepository.find_by_username(register.username)
        if _username:
            raise HTTPException(
                status_code=400, detail="Username already exists!")

        # Checking the same email
        _email = await UsersRepository.find_by_email(register.email)
        if _email:
            raise HTTPException(
                status_code=400, detail="Email already exists!")

        else:
            #  insert to tables
            await PersonRepository.create(**_person.dict())
            await UsersRepository.create(**_users.dict())
