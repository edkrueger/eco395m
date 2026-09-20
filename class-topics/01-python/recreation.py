import os
from pprint import pprint
import json

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://ridb.recreation.gov/api/v1/"
RECAREAS_ENDPOINT = BASE_URL + "recareas"

APIKEY = os.environ["APIKEY"]

HEADER = {
	"apikey": APIKEY
}

def get_recareas(activity=None, state=None, offset=None, limit=50):

	params = {}

	if activity:
		params["activity"] = activity
	if state:
		params["state"] = state
	if offset:
		params["offset"] = offset
	if limit:
		params["limit"] = limit

	r = requests.get(RECAREAS_ENDPOINT, params=params, headers=HEADER)

	r.raise_for_status()

	return r.json()["RECDATA"]


def get_all_recareas(activity=None, state=None):

	offset = 0
	all_recdata = []

	page = 0

	while True:

		page += 1

		print(f"Getting page {page}")
		
		rec_data = get_recareas(activity=activity, state=state, offset=offset)

		if not rec_data:
			print(f"Page {page} has no data. Done.")
			break

		offset += 50

		all_recdata += rec_data


	print(f"Found {len(all_recdata)} records.")

	return all_recdata

data = get_all_recareas(activity="boating")

with open("recration_results.json", "w+") as file:
	file.write(json.dumps(data))