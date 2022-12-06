from fastapi import APIRouter, Depends, Security

from app.schema import ResponseSchema, ReadPartySchema, CreatePartySchema, UpdatePartySchema, DeletePartySchema
from app.repository.auth_repo import JWTBearer, JWTRepo
from fastapi.security import HTTPAuthorizationCredentials
from app.service.parties import PartyService

router = APIRouter(
    prefix="/parties",
    tags=['party']
)


@router.post("/get_by_id", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_party(request_body: ReadPartySchema):
    result = await PartyService.get_party_by_id(request_body)
    return ResponseSchema(detail="Successfully get 1 data!", result=result)


@router.post("/get_all_users_party", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_users_party(request_body: ReadPartySchema):
    result = await PartyService.get_all_user_party(request_body)
    return ResponseSchema(detail="Successfully get all data!", result=result)


@router.post("/create", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_party(request_body: CreatePartySchema):
    result = await PartyService.create_party(request_body)
    return ResponseSchema(detail="Successfully create data!", result=result)


@router.put("/update", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_party(request_body: UpdatePartySchema):
    result = await PartyService.update_party(request_body)
    return ResponseSchema(detail="Successfully update data!", result=result)


@router.delete("/delete", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_party(request_body: DeletePartySchema):
    result = await PartyService.delete_party(request_body)
    return ResponseSchema(detail="Successfully delete data!", result=result)
