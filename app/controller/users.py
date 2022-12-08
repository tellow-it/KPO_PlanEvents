from fastapi import APIRouter, Security

from app.schema import ResponseSchema, M2MUserPartySchema
from app.repository.auth_repo import JWTBearer, JWTRepo
from fastapi.security import HTTPAuthorizationCredentials

from app.service.m2m_user_party import M2MUserPartyService
from app.service.parties import PartyService
from app.service.users import UserService
from app.service.m2m_user_bucket import M2MUserBucketService

router = APIRouter(
    prefix="/users",
    tags=['user']
)


@router.get("/", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_user_profile(credentials: HTTPAuthorizationCredentials = Security(JWTBearer())):
    token = JWTRepo.extract_token(credentials)
    result = await UserService.get_user_profile(token['username'])
    return ResponseSchema(detail="Successfully get user data!", result=result)


@router.get("/{user_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_user_profile(user_id: str):
    result = await UserService.get_user_profile_by_id(user_id)
    return ResponseSchema(detail="Successfully get user data!", result=result)


@router.get("/get_all_users", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_users():
    result = await UserService.get_all_users()
    return ResponseSchema(detail="Successfully get all user data!", result=result)


@router.get("/get_all_party/{user_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_party_for_user(user_id: str):
    parties = await M2MUserPartyService.get_all_parties_user(user_id)
    result = []
    for party in parties:
        party_info = await PartyService.get_party_by_id(party)
        result.append(party_info)
    return ResponseSchema(detail="Successfully all parties for user!", result=result)


@router.delete("/user/{user_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_user(user_id: str):
    result = await UserService.delete_user(user_id)
    await M2MUserPartyService.delete_m2m_user(user_id)
    await M2MUserBucketService.delete_user_m2m_us_bc(user_id)
    return ResponseSchema(detail="Successfully delete user_party!", result=result)


@router.delete("/exit_party", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_party(request_body: M2MUserPartySchema):
    result = await M2MUserPartyService.delete_m2m_us_pr(request_body.user_id, request_body.party_id)
    await M2MUserBucketService.delete_user_party_m2m_us_bc(request_body.user_id, request_body.party_id)
    return ResponseSchema(detail="Successfully delete user_party!", result=result)
