from uuid import uuid4
from app.model import Bucket
from app.schema import CreateBucketSchema, UpdateBucketSchema
from app.repository.buckets import BucketRepository


class BucketService:

    @staticmethod
    async def create_bucket(payload: CreateBucketSchema):
        # Create uuid
        _bucket_id = str(uuid4())

        # mapping request data to class entity table
        _bucket = Bucket(id=_bucket_id,
                         name=payload.name,
                         quantity=payload.quantity,
                         price=payload.price,
                         party_id=payload.party_id
                         )
        await BucketRepository.create(**_bucket.dict())
        return _bucket_id

    @staticmethod
    async def get_bucket_by_id(bucket_id: str):
        return await BucketRepository.get_by_id(bucket_id)

    @staticmethod
    async def get_all_buckets_party(party_id: str):
        return await BucketRepository.get_all_buckets(party_id)

    @staticmethod
    async def get_all_buckets():
        return await BucketRepository.get_all()

    @staticmethod
    async def update_bucket(payload: UpdateBucketSchema):
        return await BucketRepository.update(payload.id, **payload.dict())

    @staticmethod
    async def delete_bucket(bucket_id: str):
        return await BucketRepository.delete(bucket_id)

    @staticmethod
    async def delete_all_bucket(party_id: str):
        return await BucketRepository.delete_all_buckets_for_party(party_id)