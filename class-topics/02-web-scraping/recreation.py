import os
from pprint import pprint

from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.environ["API_KEY"]
BASE_URL = "https://ridb.recreation.gov/api/v1/"
LIMIT = 50
HEADERS = {"apikey": API_KEY}


def get_recareas_page(state, offset):

    endpoint = "recareas"

    url = BASE_URL + endpoint

    payload = {"state": state, "limit": LIMIT, "offset": offset}

    r = requests.get(url, params=payload, headers=HEADERS)

    r_json = r.json()
    data = r_json["RECDATA"]

    rec_areas = [{"name": row["RecAreaName"], "id": row["RecAreaID"]} for row in data]

    return rec_areas


def get_recareas_page_all(state):

    rec_areas = []
    offset = 0

    while True:

        new_rec_areas = get_recareas_page(state=state, offset=offset)

        if not new_rec_areas:
            break

        rec_areas += new_rec_areas
        offset += LIMIT

    return rec_areas


result = get_recareas_page_all(state="TX")
print(result)
print(len(result))
