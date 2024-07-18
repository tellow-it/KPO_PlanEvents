from fastapi import FastAPI
from auth_routers import auth_router
from party_routers import party_router
from fastapi_jwt_auth import AuthJWT
from schemas import Settings
import models
from database import Session, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    'http://localhost',
    'http://localhost:3000',
    'http://localhost:8000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@AuthJWT.load_config
def get_config():
    return Settings()


app.include_router(auth_router)
app.include_router(party_router)
