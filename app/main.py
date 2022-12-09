from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import db
from app.controller import (authentication,
                            users,
                            parties,
                            buckets,
                            m2m_user_party,
                            m2m_user_bucket)

db.init()

app = FastAPI(
    title="Party management Project",
    description="Login Page and Registration Page",
    version="1"
)
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.on_event("startup")
async def startup():
    await db.create_all()


@app.on_event("shutdown")
async def shutdown():
    await db.close()


app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(parties.router)
app.include_router(buckets.router)
app.include_router(m2m_user_party.router)
app.include_router(m2m_user_bucket.router)