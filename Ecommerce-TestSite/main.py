import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

r=requests.get(url)
# print(r)

soup=BeautifulSoup(r.content, "html.parser")
# print(soup.prettify())

# boxes=soup.find_all("div",class_="col-md-4 col-xl-4 col-lg-4")
# print(boxes)

names = soup.find_all("a",class_="title")
# print(names)

for name in names:
    print(name.text)