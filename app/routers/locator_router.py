from fastapi import APIRouter
from app.clients import WialonClient
from app.services.locator_service import LocatorService

router = APIRouter(prefix="/locator")
client = WialonClient()
service = LocatorService(client)


@router.get("/")
def get_locator(token: str = "", items: str = None):
    items = items.split(",") if items else None
    return {"locator_token": service.get_locator(token=token, items=items)}
