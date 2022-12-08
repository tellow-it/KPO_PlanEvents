from app.model.parties import Party
from app.repository.base_repo import BaseRepo


class PartyRepository(BaseRepo):
    model = Party


