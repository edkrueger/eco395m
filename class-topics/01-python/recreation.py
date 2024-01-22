import os

import requests
import dotenv

dotenv.load_dotenv()

APIKEY = os.environ["APIKEY"]
BASE_URL = "https://ridb.recreation.gov/api/v1/"
ACTIVITIES_ENDPOINT = "activities"
HEADERS = {
    "apikey": APIKEY
}

response = requests.get(url=BASE_URL+ACTIVITIES_ENDPOINT, headers=HEADERS)

print(response)
print(response.json())