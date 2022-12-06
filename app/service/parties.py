import base64
from datetime import datetime
from uuid import uuid4
from fastapi import HTTPException

from passlib.context import CryptContext

from app.model import Party
from app.schema import ReadPartySchema, UpdatePartySchema, DeletePartySchema
from app.repository.parties import PartyRepository

from app.schema import CreatePartySchema


class PartyService:

    @staticmethod
    async def create_party(payload: CreatePartySchema):
        # Create uuid
        _party_id = str(uuid4())

        # mapping request data to class entity table
        _party = Party(id=_party_id,
                       name=payload.name,
                       description=payload.description,
                       admin_id=payload.admin_id,
                       lock_bucket=payload.lock_bucket)
        await PartyRepository.create(**_party.dict())
        return _party_id

    @staticmethod
    async def get_party_by_id(payload: ReadPartySchema):
        await PartyRepository.get_by_id(payload.id)

    @staticmethod
    async def get_all_user_party(payload: ReadPartySchema):
        await PartyRepository.find_all_users_party(payload.id)

    @staticmethod
    async def update_party(payload: UpdatePartySchema):
        await PartyRepository.update(payload.id, **payload.dict())

    @staticmethod
    async def delete_party(payload: DeletePartySchema):
        await PartyRepository.delete(payload.id)
