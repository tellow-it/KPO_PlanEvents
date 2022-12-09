from fastapi import APIRouter
from app.schema import ResponseSchema
from app.service.m2m_user_party import M2MUserPartyService

router = APIRouter(
    prefix="/m2m_user_party",
    tags=['m2m_user_party'],
)


@router.get("/", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_m2m_user_party():
    result = await M2MUserPartyService.get_all_m2m()
    return ResponseSchema(detail="Successfully get bucket data!", result=result)


@router.get("/party_for_user", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_m2m_party_for_user(user_id: str):
    result = await M2MUserPartyService.get_all_parties_user(user_id)
    return ResponseSchema(detail="Successfully get bucket data!", result=result)


@router.get("/users_for_party", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_m2m_user_for_party(party_id: str):
    result = await M2MUserPartyService.get_all_users_party(party_id)
    return ResponseSchema(detail="Successfully get bucket data!", result=result)