from app.model.buckets import Bucket
from app.repository.base_repo import BaseRepo
from app.config import db, commit_rollback
from sqlalchemy.future import select
from sqlalchemy import delete as sql_delete


class BucketRepository(BaseRepo):
    model = Bucket

    @staticmethod
    async def get_all_buckets(party_id: str):
        query = select(Bucket).where(Bucket.party_id == party_id)
        return (await db.execute(query)).scalars().all()

    @staticmethod
    async def delete_all_buckets_for_party(party_id: str):
        query = sql_delete(Bucket).where(Bucket.party_id == party_id)
        await db.execute(query)
        await commit_rollback()

