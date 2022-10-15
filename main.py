from fastapi import FastAPI
from auth_routers import auth_router
from party_routers import party_router
from fastapi_jwt_auth import AuthJWT
from schemas import Settings
import models
from database import Session, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@AuthJWT.load_config
def get_config():
    return Settings()


app.include_router(auth_router)
app.include_router(party_router)
