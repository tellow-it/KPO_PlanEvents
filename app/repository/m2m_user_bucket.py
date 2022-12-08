from sqlalchemy.future import select
from app.model import M2M_User_Bucket
from app.repository.base_repo import BaseRepo
from app.config import db, commit_rollback
from sqlalchemy import delete as sql_delete


class M2MUserBucketRepository(BaseRepo):
    model = M2M_User_Bucket

    @staticmethod
    async def get_all_users_to_bucket(bucket_id: str):
        query = select(M2M_User_Bucket.user_id).where(M2M_User_Bucket.bucket_id == bucket_id)
        return (await db.execute(query)).scalars().all()

    @staticmethod
    async def get_all_buckets_for_user(user_id: str, party_id: str):
        query = select(M2M_User_Bucket.bucket_id).where(M2M_User_Bucket.user_id == user_id,
                                                        M2M_User_Bucket.party_id == party_id)
        return (await db.execute(query)).scalars().all()

    @staticmethod
    async def delete_m2m_user_bucket(user_id: str, bucket_id: str):
        query = sql_delete(M2M_User_Bucket).where(M2M_User_Bucket.user_id == user_id,
                                                  M2M_User_Bucket.bucket_id == bucket_id)
        await db.execute(query)
        await commit_rollback()
        return 'Delete ' + user_id + ' from ' + bucket_id

    @staticmethod
    async def delete_user_party_m2m_us_pr_bs(user_id: str, party_id: str):
        query = sql_delete(M2M_User_Bucket).where(M2M_User_Bucket.user_id == user_id,
                                                  M2M_User_Bucket.party_id == party_id)
        await db.execute(query)
        await commit_rollback()
        return 'Delete ' + user_id + ' from ' + party_id

    @staticmethod
    async def delete_user_from_m2m_us_pr_bs(user_id: str):
        query = sql_delete(M2M_User_Bucket).where(M2M_User_Bucket.user_id == user_id)
        await db.execute(query)
        await commit_rollback()
        return 'Delete ' + user_id

    @staticmethod
    async def delete_party_from_m2m_us_pr_bs(party_id: str):
        query = sql_delete(M2M_User_Bucket).where(M2M_User_Bucket.party_id == party_id)
        await db.execute(query)
        await commit_rollback()
        return 'Delete ' + party_id

    @staticmethod
    async def delete_bucket_from_m2m_us_pr_bs(bucket_id: str):
        query = sql_delete(M2M_User_Bucket).where(M2M_User_Bucket.bucket_id == bucket_id)
        await db.execute(query)
        await commit_rollback()
        return 'Delete ' + bucket_id
