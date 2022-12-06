from fastapi import APIRouter,Depends,Security

from app.schema import ResponseSchema, RegisterSchema, LoginSchema, ForgotPasswordSchema
from app.repository.auth_repo import JWTBearer, JWTRepo
from fastapi.security import HTTPAuthorizationCredentials
from app.service.users import UserService

router = APIRouter(
    prefix="/parties",
    tags=['party'],
    dependencies=[Depends(JWTBearer())]
)


@router.get("/", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_party(credentials: HTTPAuthorizationCredentials = Security(JWTBearer())):
    token = JWTRepo.extract_token(credentials)
    result = await UserService.get_user_profile(token['username'])
    return ResponseSchema(detail="Successfully fetch data!", result=result)


@router.get("/get_all", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_party(credentials: HTTPAuthorizationCredentials = Security(JWTBearer())):
    token = JWTRepo.extract_token(credentials)
    result = await UserService.get_user_profile(token['username'])
    return ResponseSchema(detail="Successfully fetch data!", result=result)