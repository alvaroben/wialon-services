from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv("GURTAM_API_URL", "https://hst-api.wialon.com/wialon/ajax.html")
FLEET_TOKEN = os.getenv("FLEET_TOKEN", "")
