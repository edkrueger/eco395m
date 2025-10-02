import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = "https://quotes.toscrape.com/page/"


# print(soup)

def get_divquotes_from_soup(soup):
    return soup.find_all("div", class_="quote")

def get_author_from_divquote(divquote):
    return divquote.find_all("small", class_="author")[0].text

def get_quote_from_divquote(divquote):
    return divquote.find_all("span", class_="text")[0].text

def scape_page(num):
    
    response = requests.get(URL + str(num))

    soup = BeautifulSoup(response.text)

    divquotes = get_divquotes_from_soup(soup)

    results = []

    for divquote in divquotes:

        author = get_author_from_divquote(divquote)
        quote = get_quote_from_divquote(divquote)

        row = {
            "author": author,
            "quote": quote
        }

        results.append(row)

    return results

def scrape():

    page = 1
    rows = []

    while True:
        
        new_rows = scape_page(page)

        if not new_rows:
            break

        page += 1
        rows += new_rows

    return rows


pprint(scrape())



