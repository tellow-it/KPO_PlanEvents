from uuid import UUID

from fastapi import APIRouter, Depends, Security

from app.schema import ResponseSchema, User_s_PartySchema
from app.repository.auth_repo import JWTBearer, JWTRepo
from fastapi.security import HTTPAuthorizationCredentials
from app.service.users import UserService

router = APIRouter(
    prefix="/users",
    tags=['user'],
    dependencies=[Depends(JWTBearer())]
)


@router.get("/", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_user_profile(credentials: HTTPAuthorizationCredentials = Security(JWTBearer())):
    token = JWTRepo.extract_token(credentials)
    result = await UserService.get_user_profile(token['username'])
    return ResponseSchema(detail="Successfully get user data!", result=result)


@router.get("/get_all_users", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_users():
    result = await UserService.get_all_users()
    return ResponseSchema(detail="Successfully get all user data!", result=result)


@router.get("/get_all_party/{user_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_party_for_id(user_id: str):
    result = await UserService.get_all_parties(user_id)
    return ResponseSchema(detail="Successfully all users for !", result=result)
