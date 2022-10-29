from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import db
from app.service.auth_service import generate_role

# origins = [
#     "http://localhost:3000",
#     "http://localhost:8000"
# ]


def init_app():
    db.init()

    app = FastAPI(
        title="Party management Project",
        description="Login Page and Registration Page",
        version="1"
    )
    origins = [
        'http://localhost',
        'http://localhost:3000',
        'http://localhost:8000',
        'https://party-manager-2.herokuapp.com'
    ]

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
        await generate_role()

    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    from app.controller import authentication, users

    app.include_router(authentication.router)
    app.include_router(users.router)

    return app


app = init_app()
