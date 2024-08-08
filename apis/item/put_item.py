import logging
from uuid import UUID

from fastapi import Body, Depends, HTTPException, Path
from pydantic import BaseModel, Field, model_validator
from sqlalchemy.orm import Session

from dependencies.get_db import get_db
from schemas.item_schema import ItemSchema
from utils.get_item_or_404 import get_item_or_404


class RequestBody(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
    )
    price: float | None = Field(
        default=None,
        ge=0,
    )

    @model_validator(mode="after")
    def after_model_validator(self):
        if self.name is None:
            if self.price is None:
                raise ValueError("At least one field must be updated")
        return self


def put_item(
    uuid: UUID = Path(),
    body: RequestBody = Body(),
    db: Session = Depends(get_db),
) -> ItemSchema:
    try:
        item = get_item_or_404(
            uuid=uuid,
            db=db,
        )

        if body.name is not None:
            item.name = body.name

        if body.price is not None:
            item.price = body.price

        db.commit()
        db.refresh(item)

        return ItemSchema.model_validate(item)
    except HTTPException as e:
        raise e
    except Exception as e:
        logging.error(e)
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
