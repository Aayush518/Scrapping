import requests
from bs4 import BeautifulSoup

url = "https://www.daraz.com.np/laptops/?spm=a2a0e.11779170.cate_5.4.287d2d2bJEJSDq"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

# Find the link for the next page
next_page_link = soup.find("a", class_="ant-pagination-item-link")
if next_page_link:
    next_page_href = next_page_link.get("href")
    print(next_page_href)
else:
    print("No next page link found.")
