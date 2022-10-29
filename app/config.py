from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

# DB_CONFIG = f'postgresql+asyncpg://postgres:DtnthDgjkt2002@localhost:5432/kpo_test'
DB_CONFIG = f'postgresql+asyncpg://hxydaysjpesvuk:986938a8df52beb02932528fc603d07429eab58dffaf7a8f7fc471bdd7d7e5f4@ec2-99-80-170-190.eu-west-1.compute.amazonaws.com:5432/d2u8f41ji4qhd0'

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
