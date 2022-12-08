from sqlalchemy.future import select
from app.model import Users, Person
from app.config import db
from app.repository.users import UsersRepository


class UserService:

    @staticmethod
    async def get_user_profile(username: str):
        query = select(
            Users.id,
            Users.username,
            Users.email,
            Person.name,
            Person.birth,
            Person.sex,
            Person.phone_number).join_from(Users, Person).where(Users.username == username)
        return (await db.execute(query)).mappings().one()

    @staticmethod
    async def get_user_profile_by_id(user_id: str):
        query = select(
            Users.id,
            Users.username,
            Users.email).where(Users.id == user_id)
        return (await db.execute(query)).scalar()

    @staticmethod
    async def get_all_users():
        return await UsersRepository.get_all()

    @staticmethod
    async def delete_user(user_id: str):
        return await UsersRepository.delete(user_id)

