from app.model.buckets import Bucket
from app.repository.base_repo import BaseRepo
from app.config import db
from sqlalchemy.future import select


class BucketRepository(BaseRepo):
    model = Bucket

    @staticmethod
    async def get_all_buckets(party_id: str):
        query = select(Bucket).where(Bucket.party_id == party_id)
        return (await db.execute(query)).scalars().all()
