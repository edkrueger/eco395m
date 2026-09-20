import csv
from pprint import pprint

import requests

BASE_URL = "https://uselessfacts.jsph.pl/api/v2/facts/"
RANDOM_ENDPOINT = BASE_URL + "random"
TODAY_ENDPOINT = BASE_URL + "random"


def random_fact(language):
	params = {
		"language": language
	}
	r = requests.get(RANDOM_ENDPOINT, params=params)
	r.raise_for_status()
	fact = r.json()
	return fact

def get_facts(max_requests=100, language="en"):

	ids = set()
	facts = []

	for i in range(max_requests):

		print(f"Doing request: {i+1}")

		fact_dict = random_fact(language)
		id_ = fact_dict["id"]

		if not id_ in ids:
			ids.add(id)
			facts.append(fact_dict)

	print(f"Found {len(facts)} facts!")

	return facts

def write_facts(facts, path="uselessfacts.csv"):

	with open(path, "w+") as file:
		
		csv_writer = csv.DictWriter(file, fieldnames=["id", "text", "source", "source_url", "language", "permalink"])

		for fact in facts:
			csv_writer.writerow(fact)

facts = get_facts(max_requests=20)
facts_de = get_facts(max_requests=20, language="de")
all_facts = facts + facts_de
write_facts(all_facts)