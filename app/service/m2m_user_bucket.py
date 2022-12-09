from uuid import uuid4
from app.model import M2M_User_Bucket
from app.repository.m2m_user_bucket import M2MUserBucketRepository
from app.schema import M2MUserBucketSchema


class M2MUserBucketService:

    @staticmethod
    async def get_all_m2m():
        return await M2MUserBucketRepository.get_all()

    @staticmethod
    async def get_all_buckets_for_user(user_id: str, party_id: str):
        return await M2MUserBucketRepository.get_all_buckets_for_user(user_id, party_id)

    @staticmethod
    async def create_party(user_id: str, bucket_id: str, party_id: str):
        # mapping request data to class entity table
        _id = str(uuid4())
        _m2m_user_bucket = M2M_User_Bucket(id=_id,
                                           user_id=user_id,
                                           bucket_id=bucket_id,
                                           party_id=party_id)
        return await M2MUserBucketRepository.create(**_m2m_user_bucket.dict())

    @staticmethod
    async def get_all_users_bucket(bucket_id: str):
        return await M2MUserBucketRepository.get_all_users_to_bucket(bucket_id)

    @staticmethod
    async def delete_user_from_bucket(request_body: M2MUserBucketSchema):
        return await M2MUserBucketRepository.delete_user_from_bucket(request_body)

    @staticmethod
    async def delete_m2m_us_bc(user_id: str, bucket_id: str, party_id: str):
        return await M2MUserBucketRepository.delete_m2m_user_bucket(user_id, bucket_id, party_id)

    @staticmethod
    async def delete_user_party_m2m_us_bc(user_id: str, party_id: str):
        return await M2MUserBucketRepository.delete_user_party_m2m_us_pr_bs(user_id, party_id)

    @staticmethod
    async def delete_user_m2m_us_bc(user_id: str):
        return await M2MUserBucketRepository.delete_user_from_m2m_us_pr_bs(user_id)

    @staticmethod
    async def delete_party_m2m_us_bc(party_id: str):
        return await M2MUserBucketRepository.delete_party_from_m2m_us_pr_bs(party_id)

    @staticmethod
    async def delete_bucket_m2m_us_bc(bucket_id: str):
        return await M2MUserBucketRepository.delete_bucket_from_m2m_us_pr_bs(bucket_id)
