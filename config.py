from os import getenv

from dotenv import load_dotenv

load_dotenv()

api_base_url = getenv("API_URL", "https://catfact.ninja")
request_timeout = getenv("API_REQUEST_TIMEOUT", 10)
