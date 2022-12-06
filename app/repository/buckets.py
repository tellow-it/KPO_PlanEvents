from app.model.buckets import Bucket
from app.repository.base_repo import BaseRepo


class BucketRepository(BaseRepo):
    model = Bucket
