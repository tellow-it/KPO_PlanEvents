from uuid import uuid4
from app.model import M2M_User_Party
from app.repository.m2m_user_party import M2MUserPartyRepository


class M2MUserPartyService:

    @staticmethod
    async def get_all_m2m():
        return await M2MUserPartyRepository.get_all()

    @staticmethod
    async def create_party(user_id: str, party_id: str):
        # mapping request data to class entity table
        _id = str(uuid4())
        _m2m_user_party = M2M_User_Party(id=_id,
                                         user_id=user_id,
                                         party_id=party_id)
        return await M2MUserPartyRepository.create(**_m2m_user_party.dict())

    @staticmethod
    async def get_all_parties_user(user_id: str):
        return await M2MUserPartyRepository.get_all_parties_user(user_id)

    @staticmethod
    async def get_all_users_party(party_id: str):
        return await M2MUserPartyRepository.get_all_users_party(party_id)

    @staticmethod
    async def delete_m2m_us_pr(user_id: str, party_id: str):
        return await M2MUserPartyRepository.delete_m2m_user_party(user_id, party_id)

    @staticmethod
    async def delete_m2m_party(party_id: str):
        return await M2MUserPartyRepository.delete_m2m_party(party_id)

    @staticmethod
    async def delete_m2m_user(user_id: str):
        return await M2MUserPartyRepository.delete_m2m_user(user_id)