from uuid import UUID

from pydantic import Field

from schemas.base_schema import BaseSchema


class ItemSchema(BaseSchema):
    uuid: UUID
    name: str = Field(
        min_length=1,
        max_length=255,
    )
    price: float = Field(
        ge=0,
    )
