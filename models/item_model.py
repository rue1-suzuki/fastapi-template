from uuid import uuid4

from sqlalchemy import Column, Float, String, Uuid

from database import Base


class Item(Base):
    __tablename__ = "items"

    uuid = Column(
        type_=Uuid(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )
    name = Column(
        type_=String(255),
        nullable=False,
    )
    price = Column(
        type_=Float,
        nullable=False,
    )
