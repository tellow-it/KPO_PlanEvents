from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

# DB_CONFIG = f'postgresql+asyncpg://postgres:DtnthDgjkt2002@localhost:5432/kpo_test'
# DB_CONFIG = f'postgresql+asyncpg://vagllbujtngaby:b8e2f14be242b6f239ecb9f8cbbcb3c1b621c8ec5dc2c28613b5b03bb45b9d9f@ec2-176-34-215-248.eu-west-1.compute.amazonaws.com:5432/d6jmr629n0q553'
DB_CONFIG = f'postgresql+asyncpg://kpo_party_manager_db_wzfe_user:TfsSAhZPkiugmmpeTdgptQuRExAMNGPo@dpg-ce9iudsgqg4bcbgigbs0-a/kpo_party_manager_db_wzfe'

SECRET_KEY = "kpo_project"
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class AsyncDatabaseSession:

    def __init__(self) -> None:
        self.session = None
        self.engine = None

    def __getattr__(self, name):
        return getattr(self.session, name)

    def init(self):
        self.engine = create_async_engine(DB_CONFIG, future=True, echo=True)
        self.session = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)()

    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)


db = AsyncDatabaseSession()


async def commit_rollback():
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise
