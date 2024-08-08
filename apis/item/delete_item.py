import logging
from uuid import UUID

from fastapi import Depends, HTTPException, Path, Response
from sqlalchemy.orm import Session

from dependencies.get_db import get_db
from utils.get_item_or_404 import get_item_or_404


def delete_item(
    uuid: UUID = Path(),
    db: Session = Depends(get_db),
) -> None:
    try:
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
    except HTTPException as e:
        raise e
    except Exception as e:
        logging.error(e)
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
