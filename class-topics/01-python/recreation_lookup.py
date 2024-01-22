import os
import csv
from functools import cache

import requests
import dotenv

dotenv.load_dotenv()

OUTPUT_DIR = "artifacts"
FILENAME = "rec_areas.csv"
FILEPATH = os.path.join(OUTPUT_DIR, FILENAME)

os.makedirs(OUTPUT_DIR, exist_ok=True)

APIKEY = os.environ["APIKEY"]
BASE_URL = "https://ridb.recreation.gov/api/v1/"
ACTIVITIES_ENDPOINT = "activities"
REC_AREAS_ENDPOINT = "recareas"

HEADERS = {
    "apikey": APIKEY
}

def get_activities():

    limit = 50
    offset = 0
    data = []

    dry_response = requests.get(url=BASE_URL+ACTIVITIES_ENDPOINT, headers=HEADERS, params={
    "limit": 1,
})
    
    total_count = dry_response.json()["METADATA"]["RESULTS"]["TOTAL_COUNT"]

    while offset < total_count:
        response = requests.get(url=BASE_URL+ACTIVITIES_ENDPOINT, headers=HEADERS, params={
    "limit": limit,
    "offset": offset
})
        

        new_data = response.json()["RECDATA"]
        data += new_data
        offset += limit
    
    return data

@cache
def make_activities_lookup():


    activities = get_activities()

    dict_ = {}

    for activity in activities:

        activity_id = activity["ActivityID"]
        activity_name = activity["ActivityName"]

        dict_[activity_name] = activity_id

    return dict_

def lookup_rec_areas(activity, state_code):

    activities_lookup = make_activities_lookup()

    if not activity in activities_lookup:
        raise ValueError("Activity not found!")
    
    activity_id = activities_lookup[activity]
    

    response = requests.get(url=BASE_URL + REC_AREAS_ENDPOINT, headers=HEADERS, params={
        "limit": 50,
        "offset": 0,
        "state": state_code,
        "activity": activity_id
    })

    data = response.json()["RECDATA"]

    return [{"name": d["RecAreaName"], "desc":d["RecAreaDescription"]  }for d in data]

def write_clean_rec_areas(clean_data):

    fieldnames = ["name", "desc"]

    with open(FILEPATH, "w+") as f:

        dict_writer = csv.DictWriter(f=f, fieldnames=fieldnames)
        dict_writer.writeheader()

    
        dict_writer.writerows(clean_data)

data = lookup_rec_areas(activity="BOATING", state_code="TX")
write_clean_rec_areas(data)