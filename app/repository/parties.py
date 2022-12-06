from app.model.parties import Party
from app.repository.base_repo import BaseRepo


class PartyRepository(BaseRepo):
    model = Party

    @staticmethod
    async def find_all_users_party(party_id: str):
        # query = получить всех юзеров из связной таблицы по id
        # return (await db.execute(query)).scalars().all()
        pass

