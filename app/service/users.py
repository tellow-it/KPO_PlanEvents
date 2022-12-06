from sqlalchemy.future import select
from app.model import Users, Person
from app.config import db


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
    async def get_all_parties(id: str):
        # query = # из связной таблицы по id юзера получить все мероприятия для этого юзера
        # return = (await db.execute(query)).scalars.all()
        pass
