from uuid import UUID

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
    async def get_all_users():
        return await UsersRepository.get_all()

    @staticmethod
    async def get_all_parties(party_id: UUID):
        # query = # из связной таблицы по id юзера получить все мероприятия для этого юзера
        # return = (await db.execute(query)).scalars.all()
        pass
