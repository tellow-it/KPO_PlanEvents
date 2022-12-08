from fastapi import APIRouter
from app.schema import ResponseSchema, CreateBucketSchema, UpdateBucketSchema, M2MUserBucketSchema
from app.service.buckets import BucketService
from app.service.m2m_user_bucket import M2MUserBucketService

router = APIRouter(
    prefix="/buckets",
    tags=['bucket'],
)


@router.get("/", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_buckets():
    result = await BucketService.get_all_buckets()
    return ResponseSchema(detail="Successfully get bucket data!", result=result)


@router.get("/{bucket_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_bucket(bucket_id: str):
    result = await BucketService.get_bucket_by_id(bucket_id)
    return ResponseSchema(detail="Successfully get bucket data!", result=result)


@router.get("/get_all_buckets_party/{party_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_buckets(party_id: str):
    result = await BucketService.get_all_buckets_party(party_id)
    return ResponseSchema(detail="Successfully get all bucket for party!", result=result)


@router.get("/get_total_price/{party_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_buckets(party_id: str):
    buckets = await BucketService.get_all_buckets_party(party_id)
    result = 0
    for bc in buckets:
        result += bc['quantity'] * bc['price']
    return ResponseSchema(detail="Successfully get total sum for party!", result=result)


@router.get("/get_price_for_user/{user_id}&{party_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_price_for_user(user_id: str, party_id: str):
    buckets = await M2MUserBucketService.get_all_buckets_for_user(user_id, party_id)
    result = []
    for bc in buckets:
        bucket_info = await BucketService.get_bucket_by_id(bc)
        bucket_info['number_people'] = len(await M2MUserBucketService.get_all_users_bucket(bc))
        bucket_info['price_for_user'] = bucket_info['quantity'] * bucket_info['price'] / bucket_info['number_people']
        result.append(bucket_info)

    return ResponseSchema(detail="Successfully get total sum for party!", result=result)


@router.post("/create", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_bucket(request_body: CreateBucketSchema):
    result = await BucketService.create_bucket(request_body)
    return ResponseSchema(detail="Successfully create data!", result=result)


@router.post("/add_user", response_model=ResponseSchema, response_model_exclude_none=True)
async def add_user(request_body: M2MUserBucketSchema):
    result = await M2MUserBucketService.create_party(request_body.user_id,
                                                     request_body.bucket_id,
                                                     request_body.party_id)

    return ResponseSchema(detail="Successfully add user!", result=result)


@router.delete("/remove_user_from_bucket", response_model=ResponseSchema, response_model_exclude_none=True)
async def remove_user(request_body: M2MUserBucketSchema):
    result = await M2MUserBucketService.delete_m2m_us_bc(request_body.user_id, request_body.bucket_id)
    return ResponseSchema(detail="Successfully add user!", result=result)


@router.put("/update", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_bucket(request_body: UpdateBucketSchema):
    result = await BucketService.update_bucket(request_body)
    return ResponseSchema(detail="Successfully update data!", result=result)


@router.delete("/delete/{bucket_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_bucket(bucket_id: str):
    result = await BucketService.delete_bucket(bucket_id)
    await M2MUserBucketService.delete_bucket_m2m_us_bc(bucket_id)
    return ResponseSchema(detail="Successfully delete data!", result=result)
