from fastapi import APIRouter, Depends, Security

from app.schema import ResponseSchema, RegisterSchema, LoginSchema, ForgotPasswordSchema
from app.repository.auth_repo import JWTBearer, JWTRepo
from fastapi.security import HTTPAuthorizationCredentials
from app.service.users import UserService

router = APIRouter(
    prefix="/buckets",
    tags=['bucket'],
)


@router.get("/", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_bucket():
    return ResponseSchema(detail="Successfully fetch data!")
