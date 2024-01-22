import requests
from bs4 import BeautifulSoup

def get_soup_from_page_num(page_num):


    url = f"http://quotes.toscrape.com/page/{page_num}/"

    response = requests.get(url)

    html = response.text

    soup = BeautifulSoup(html)

    return soup

def get_quote_divs(soup):
    return soup.find_all("div", class_="quote")


def extract_quote_div(quote_div):
    quote = quote_div.find_all("span", class_="text")[0].string
    author_small = quote_div.find_all("small", class_="author")[0]
    author = author_small.string
    author_link = "http://quotes.toscrape.com" + author_small.parent.a["href"]
    tags_div =  quote_div.find_all("div", class_ ="tags")[0]
    tags = [a.string for a in tags_div.find_all("a", class_="tag")]

    return {
        "quote": quote,
        "author": author,
        "author_link": author_link,
        "tags": tags
    }

def scape_page(page_num):

    soup = get_soup_from_page_num(page_num)

    return [extract_quote_div(quote_div) for quote_div  in get_quote_divs(soup)]

def scrape_pages():

    current_page = 1
    data = []

    while True:

        new_data = scape_page(current_page)

        if not new_data:
            break

        data += new_data
        current_page += 1
    
    return data


if __name__ == "__main__":
    import pprint


    pprint.pprint(scrape_pages())
