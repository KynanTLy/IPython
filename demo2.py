
import requests

from bs4 import BeautifulSoup, NavigableString

page = requests.get('https://en.wikipedia.org/wiki/Mid-Autumn_Festival#Mooncakes')

soup = BeautifulSoup(page.text, 'html.parser')

text = [i for i in soup.recursiveChildGenerator() if type(i) == NavigableString]

print(text)
