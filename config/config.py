from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL: str = "https://ru.yougile.com/api-v2"
UI_URL: str = "https://ru.yougile.com"

API_KEY: str = os.getenv("API_KEY")