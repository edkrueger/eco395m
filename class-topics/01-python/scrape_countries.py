from pprint import pprint

import requests
from bs4 import BeautifulSoup

URL = "https://www.scrapethissite.com/pages/simple/"

r = requests.get(URL)
r.raise_for_status()
html = r.text

soup = BeautifulSoup(html)

country_cards = soup.find_all(class_="country")

print(country_cards[0])

rows = []
for country_card in country_cards:

	row = {
		"country": country_card.find(class_="country-name").text.strip(),
		"capitol": country_card.find(class_="country-capital").text.strip(),
		"population": country_card.find(class_="country-population").text.strip(),
		"area": country_card.find(class_="country-area").text.strip(),
	}

	rows.append(row)

pprint(rows)



