from fastapi import APIRouter

from apis.item.delete_item import delete_item
from apis.item.get_item import get_item
from apis.item.list_item import list_item
from apis.item.post_item import post_item
from apis.item.put_item import put_item

item_router = APIRouter(tags=["items"])
item_router.add_api_route(
    path="/items",
    endpoint=list_item,
    methods=["GET"],
)
item_router.add_api_route(
    path="/items",
    endpoint=post_item,
    methods=["POST"],
)
item_router.add_api_route(
    path="/items/{uuid}",
    endpoint=get_item,
    methods=["GET"],
)
item_router.add_api_route(
    path="/items/{uuid}",
    endpoint=put_item,
    methods=["PUT"],
)
item_router.add_api_route(
    path="/items/{uuid}",
    endpoint=delete_item,
    methods=["DELETE"],
)
