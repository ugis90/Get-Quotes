import requests
import bs4

res = requests.get("http://quotes.toscrape.com/")

bs = bs4.BeautifulSoup(res.text, "lxml")

quotes = bs.select(".text")
quotes = [quote.text for quote in quotes]

top_tags = bs.select(".tag-item")

base_url = "http://quotes.toscrape.com/page/{}/"
i = 1
while True:
    res = requests.get(base_url.format(i))
    bs = bs4.BeautifulSoup(res.text, "lxml")
    quotes = bs.select(".text")
    for quote in quotes:
        print(quote.text)
    i += 1
    if(len(quotes) == 0):
        break