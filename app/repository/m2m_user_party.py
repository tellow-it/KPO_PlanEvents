from sqlalchemy.future import select
from app.model import M2M_User_Party
from app.repository.base_repo import BaseRepo
from app.config import db, commit_rollback
from sqlalchemy import delete as sql_delete


class M2MUserPartyRepository(BaseRepo):
    model = M2M_User_Party

    @staticmethod
    async def get_all_parties_user(user_id: str):
        query = select(M2M_User_Party).where(M2M_User_Party.user_id == user_id)
        return (await db.execute(query)).scalars().all()

    @staticmethod
    async def get_all_users_party(party_id: str):
        query = select(M2M_User_Party.user_id).where(M2M_User_Party.party_id == party_id)
        return (await db.execute(query)).scalars().all()

    @staticmethod
    async def delete_m2m_user_party(user_id: str, party_id: str):
        query = sql_delete(M2M_User_Party).where(M2M_User_Party.user_id == user_id,
                                                 M2M_User_Party.party_id == party_id)
        await db.execute(query)
        await commit_rollback()
        return 'Delete ' + user_id + ' from ' + party_id

    @staticmethod
    async def delete_m2m_party(party_id: str):
        query = sql_delete(M2M_User_Party).where(M2M_User_Party.party_id == party_id)
        await db.execute(query)
        await commit_rollback()
        return 'Delete ' + party_id

    @staticmethod
    async def delete_m2m_user(user_id: str):
        query = sql_delete(M2M_User_Party).where(M2M_User_Party.user_id == user_id)
        await db.execute(query)
        await commit_rollback()
        return 'Delete ' + user_id
