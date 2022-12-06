from fastapi import APIRouter, Depends, Security

from app.schema import ResponseSchema, CreateBucketSchema, ReadBucketSchema, UpdateBucketSchema, DeleteBucketSchema, ReadPartySchema
from app.repository.auth_repo import JWTBearer, JWTRepo
from fastapi.security import HTTPAuthorizationCredentials
from app.service.buckets import BucketService

router = APIRouter(
    prefix="/buckets",
    tags=['bucket'],
)


@router.get("/get_by_id", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_bucket(request_body: ReadBucketSchema):
    result = await BucketService.get_bucket_by_id(request_body)
    return ResponseSchema(detail="Successfully get 1 data!", result=result)


@router.get("/get_all_busckets", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_buckets(request_body: ReadPartySchema):
    result = await BucketService.get_all_buckets(request_body)
    return ResponseSchema(detail="Successfully get all data!", result=result)


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
