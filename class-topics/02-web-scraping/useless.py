import requests

BASE_URL = "https://uselessfacts.jsph.pl/api/v2/facts/random"

def useless_fact(language):


	payload={"language": language}

	response = requests.get(BASE_URL, params=payload)

	# print(response.url)
	# print(response.status_code)
	# print(response.text)
	# print(type(response.text))
	# print(response.json())
	data = response.json()

	return data["text"]



print(useless_fact(language="de"))