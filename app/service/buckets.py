import base64
from datetime import datetime
from uuid import uuid4
from fastapi import HTTPException

from app.model import Bucket
from app.schema import CreateBucketSchema, ReadBucketSchema, UpdateBucketSchema, DeleteBucketSchema, ReadPartySchema
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
                         )
        await BucketRepository.create(**_bucket.dict())
        return _bucket_id

    @staticmethod
    async def get_bucket_by_id(payload: ReadBucketSchema):
        await BucketRepository.get_by_id(payload.id)

    @staticmethod
    async def get_all_buckets(payload: ReadPartySchema):
        await BucketRepository.get_all_buckets(payload.id)

    @staticmethod
    async def update_bucket(payload: UpdateBucketSchema):
        await BucketRepository.update(payload.id, **payload.dict())

    @staticmethod
    async def delete_bucket(payload: DeleteBucketSchema):
        await BucketRepository.delete(payload.id)
