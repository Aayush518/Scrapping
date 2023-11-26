import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

r=requests.get(url)
# print(r)

soup=BeautifulSoup(r.content, "html.parser")
# print(soup.prettify())