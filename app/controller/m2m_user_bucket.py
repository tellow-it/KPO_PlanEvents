from fastapi import APIRouter
from app.schema import ResponseSchema
from app.service.m2m_user_bucket import M2MUserBucketService

router = APIRouter(
    prefix="/m2m_user_bucket",
    tags=['m2m_user_bucket'],
)


@router.get("/", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_m2m_user_bucket():
    result = await M2MUserBucketService.get_all_m2m()
    return ResponseSchema(detail="Successfully get bucket data!", result=result)
