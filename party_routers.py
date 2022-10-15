from fastapi import APIRouter

party_router = APIRouter(
    prefix='/parties',
    tags=['parties'])


@party_router.get('/')
async def hello():
    return {'message': 'Hello party'}
