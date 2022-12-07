from uuid import UUID

from fastapi import APIRouter, Depends, Security

from app.schema import ResponseSchema, CreateBucketSchema, ReadBucketSchema, UpdateBucketSchema, DeleteBucketSchema, \
    ReadPartySchema
from app.repository.auth_repo import JWTBearer, JWTRepo
from fastapi.security import HTTPAuthorizationCredentials
from app.service.buckets import BucketService

router = APIRouter(
    prefix="/buckets",
    tags=['bucket'],
    dependencies=[Depends(JWTBearer())]
)


@router.get("/", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_buckets():
    result = await BucketService.get_all_buckets()
    return ResponseSchema(detail="Successfully get bucket data!", result=result)


@router.get("/{bucket_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_bucket(bucket_id: UUID):
    result = await BucketService.get_bucket_by_id(bucket_id)
    return ResponseSchema(detail="Successfully get bucket data!", result=result)


@router.get("/get_all_buckets_party/{party_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_buckets(party_id: UUID):
    result = await BucketService.get_all_buckets_party(party_id)
    return ResponseSchema(detail="Successfully get all bucket for party!", result=result)


@router.post("/create", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_bucket(request_body: CreateBucketSchema):
    result = await BucketService.create_bucket(request_body)
    return ResponseSchema(detail="Successfully create data!", result=result)


@router.put("/update", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_bucket(request_body: UpdateBucketSchema):
    result = await BucketService.update_bucket(request_body)
    return ResponseSchema(detail="Successfully update data!", result=result)


@router.delete("/delete", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_bucket(request_body: DeleteBucketSchema):
    result = await BucketService.delete_bucket(request_body)
    return ResponseSchema(detail="Successfully delete data!", result=result)
