import requests
from bs4 import BeautifulSoup

URL = "http://quotes.toscrape.com/page/1/"

r = requests.get(URL)
html = r.text

soup = BeautifulSoup(html)
print(soup.prettify())

print(soup.html.head.title.text)

print(len(soup.find_all("div", class_="quote")))