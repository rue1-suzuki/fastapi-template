import pytest
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from dependencies.get_db import get_db
from models.item_model import Item
from tests.client import client


async def _create_item(
    db: Session,
    name: str = "Test Item",
    price: float = 1.0,
):
    item = Item()
    item.name = name
    item.price = price

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


def test_list_item():
    response = client.get(
        url="/items",
    )
    assert response.status_code == 200

    response_data = response.json()
    assert isinstance(response_data, list)


def test_post_item():
    response = client.post(
        url="/items",
        json={
            "name": "Test Item",
            "price": 1.0,
        },
    )
    assert response.status_code == 200

    response_data = response.json()
    assert isinstance(response_data, dict)


@pytest.mark.asyncio
async def test_get_item():
    db = await anext(get_db())
    item = await _create_item(db)

    response = client.get(
        url=f"/items/{item.uuid}",
    )
    assert response.status_code == 200

    response_data = response.json()
    assert isinstance(response_data, dict)
    assert response_data["uuid"] == str(item.uuid)
    assert response_data["name"] == item.name
    assert response_data["price"] == item.price


@pytest.mark.asyncio
async def test_put_item():
    db = await anext(get_db())
    item = await _create_item(db)

    new_name = "New Test Item"
    new_price = 2.0

    response = client.put(
        url=f"/items/{item.uuid}",
        json={
            "name": new_name,
            "price": new_price,
        },
    )
    assert response.status_code == 200

    response_data = response.json()
    assert isinstance(response_data, dict)
    assert response_data["uuid"] == str(item.uuid)
    assert response_data["name"] == new_name
    assert response_data["price"] == new_price


@pytest.mark.asyncio
async def test_delete_item():
    db = await anext(get_db())
    item = await _create_item(db)

    response = client.delete(
        url=f"/items/{item.uuid}",
    )
    assert response.status_code == 204

    try:
        db.refresh(item)
        assert False
    except InvalidRequestError:
        assert True
