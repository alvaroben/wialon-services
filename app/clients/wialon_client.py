import time
import json
import logging
import requests
from app.config import API_URL, FLEET_TOKEN

_logger = logging.getLogger(__name__)


class WialonClient:
    def __init__(self):
        self.api_url = API_URL
        self.session_uid = None
        self.last_activity = None

    def _login(self):
        if not self.session_uid or (time.time() - self.last_activity) > 300:
            _logger.info("Getting new session")
            parameters = {
                "svc": "token/login",
                "params": json.dumps({"token": FLEET_TOKEN}),
            }
            response = requests.post(self.api_url, params=parameters).json()
            if "eid" in response:
                self.session_uid = response["eid"]
                self.last_activity = time.time()
                _logger.info("Session obtained")
            else:
                _logger.error(f"Error trying get session: {response.get('reason')}")
        return self.session_uid

    def post(self, svc: str, payload: dict):
        params = {
            "svc": svc,
            "params": json.dumps(payload),
            "sid": self._login(),
        }
        response = requests.post(self.api_url, params=params)
        self.last_activity = time.time()
        return response.json()
