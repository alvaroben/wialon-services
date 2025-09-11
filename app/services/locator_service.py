from app.clients.wialon_client import WialonClient


class LocatorService:
    def __init__(self, client: WialonClient):
        self.client = client

    def get_locator(self, token="", items=None):
        if items is None:
            items = []
        payload = {
            "callMode": "create",
            "h": token,
            "app": "locator",
            "at": 0,
            "dur": 0,
            "fl": -1,
            "p": '{"note":"","zones":0,"tracks":0}',
            "items": items,
        }
        result = self.client.post(svc="token/update", payload=payload)
        return result.get("h", False)
