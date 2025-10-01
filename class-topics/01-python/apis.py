import os
from pprint import pprint

from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.environ["API_KEY"]

BASE_URL = "https://ridb.recreation.gov/api/v1/"

ACTIVITIES_ENDPOINT = BASE_URL + "activities"
RECAREAS_ENDPOINT = BASE_URL + "recareas"

HEADERS = {
    "apikey": API_KEY
}


def _get_activities(query=None, limit=50, offset=0):

    params = {
        "query": query,
        "limit": limit,
        "offset": offset
    }

    response = requests.get(ACTIVITIES_ENDPOINT, params=params, headers=HEADERS)

    response_json = response.json()

    return response_json["RECDATA"]

def get_activities(query=None):

    data = []
    offset = 0
    should_continue = True

    while should_continue:
        
        new_data = _get_activities(offset=offset)
        data += new_data
        offset += 50

        if not new_data:
            should_continue = False

    return data

def _get_recareas(query=None, limit=50, offset=0):

    params = {
        "query": query,
        "limit": limit,
        "offset": offset
    }

    response = requests.get(RECAREAS_ENDPOINT, params=params, headers=HEADERS)

    response_json = response.json()

    return response_json["RECDATA"]

def get_recareas(query=None):

    data = []
    offset = 0
    should_continue = True

    while should_continue:
        
        new_data = _get_recareas(offset=offset)
        data += new_data
        offset += 50

        if not new_data:
            should_continue = False

    return data
recareas = get_recareas()
print(len(recareas))
pprint(recareas)