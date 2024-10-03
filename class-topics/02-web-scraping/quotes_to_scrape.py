import requests
from bs4 import BeautifulSoup

URL = "http://quotes.toscrape.com/page/"

def get_quote_cards_from_soup(soup):
    """Return a list of quote elements/subtrees"""
    return soup.find_all("div", class_="quote")

def get_quote_from_quote_card(quote_card):
    """Return the quote in the car as text"""
    return quote_card.find_all("span", class_="text")[0].text

def get_author_from_quote_card(quote_card):
    """Return the author in the car as text"""
    return quote_card.find_all("small", class_="author")[0].text

def get_tags_from_quote_card(quote_card):
    """Return the tags in the car as list of strings"""
    return [tag.text for tag in quote_card.find_all("a", class_="tag")]

def get_data_from_quote_card(quote_card):
    """Return a dict with keys: quote, author, tags"""
    return {
        "quote": get_quote_from_quote_card(quote_card),
        "author": get_author_from_quote_card(quote_card),
        "tags": get_tags_from_quote_card(quote_card)
    }

def scrape_page(page_number):

    url = URL + str(page_number)

    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html)

    quote_cards = get_quote_cards_from_soup(soup)

    return [get_data_from_quote_card(quote_card) for quote_card in quote_cards]

def scrape():

    page = 1

    data = []

    while True:

        page_data = scrape_page(page)

        if not page_data:
            break

        page += 1
        data += page_data

    print(page)
    return data

data = scrape()
print(data[-5:])
print(len(data))