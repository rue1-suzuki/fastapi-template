from uuid import UUID

from fastapi import Depends, Path, Response
from sqlalchemy.orm import Session

from dependencies.get_db import get_db
from utils.get_item_or_404 import get_item_or_404


def delete_item(
    uuid: UUID = Path(),
    db: Session = Depends(get_db),
) -> None:
    item = get_item_or_404(
        uuid=uuid,
        db=db,
    )

    db.delete(item)
    db.commit()

    return Response(
        content=None,
        status_code=204,
    )
