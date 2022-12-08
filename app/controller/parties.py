from fastapi import APIRouter
from app.schema import ResponseSchema, CreatePartySchema, UpdatePartySchema, M2MUserPartySchema
from app.service.parties import PartyService
from app.service.m2m_user_party import M2MUserPartyService
from app.service.buckets import BucketService

router = APIRouter(
    prefix="/parties",
    tags=['party']
)


@router.get("/", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all():
    result = await PartyService.get_all()
    return ResponseSchema(detail="Successfully get all data!", result=result)


@router.get("/{party_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_party(party_id: str):
    result = await PartyService.get_party_by_id(party_id)
    return ResponseSchema(detail="Successfully get 1 data!", result=result)


@router.get("/get_all_users_party/{party_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_users_party(party_id: str):
    result = await M2MUserPartyService.get_all_users_party(party_id)
    return ResponseSchema(detail="Successfully get all users for party!", result=result)


@router.post("/create", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_party(request_body: CreatePartySchema):
    result = await PartyService.create_party(request_body)
    return ResponseSchema(detail="Successfully create data!", result=result)


@router.post("/add_user", response_model=ResponseSchema, response_model_exclude_none=True)
async def add_user(request_body: M2MUserPartySchema):
    result = await M2MUserPartyService.create_party(request_body.user_id, request_body.party_id)
    return ResponseSchema(detail="Successfully add user!", result=result)


@router.put("/update", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_party(request_body: UpdatePartySchema):
    result = await PartyService.update_party(request_body)
    return ResponseSchema(detail="Successfully update data!", result=result)


@router.delete("/delete/{party_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_party(party_id: str):
    result = await PartyService.delete_party(party_id)
    await M2MUserPartyService.delete_m2m_party(party_id)
    await BucketService.delete_all_bucket(party_id)
    return ResponseSchema(detail="Successfully delete data!", result=result)


@router.delete("/delete_user", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_user(request_body: M2MUserPartySchema):
    result = await M2MUserPartyService.delete_m2m_us_pr(request_body.user_id, request_body.party_id)
    return ResponseSchema(detail="Successfully delete user_party!", result=result)
