from app.model.buckets import Bucket
from app.repository.base_repo import BaseRepo


class BucketRepository(BaseRepo):
    model = Bucket

    @staticmethod
    async def get_all_buckets(party_id: str):
        # query = получить все корзины из связной таблицы по id мероприятия
        # return (await db.execute(query)).scalars().all()
        pass
