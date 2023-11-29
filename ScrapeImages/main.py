from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests as rq
from bs4 import BeautifulSoup
import os

options = Options()
options.add_experimental_option("detach", True)

# Use the absolute path for the ChromeDriver executable
path = "/usr/local/bin/chromedriver"
s=Service(path)
url = input("Enter URL: ")

output = "output"

def get_url(path, url):
    driver = webdriver.Chrome(options=options,service=s)
    driver.get(url)
    
    # Use WebDriverWait instead of time.sleep
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    
    print("Page loaded successfully")
    res = driver.page_source
    return res

def get_img_links(res):
    soup = BeautifulSoup(res, "html.parser")
    imglinks = soup.find_all("img", src=True)
    return imglinks

def download_img(img_link, index, base_url):
    try:
        # Use os.path.splitext to get the file extension
        _, extension = os.path.splitext(img_link)

        # If the URL is relative, prepend the base_url
        if img_link.startswith('/'):
            img_link = base_url + img_link

        img_data = rq.get(img_link).content
        with open(os.path.join(output, str(index + 1) + extension), "wb+") as f:
            f.write(img_data)

    except Exception as e:
        # Print or log the exception details for debugging
        print(f"Error downloading image {index + 1}: {str(e)}")


if not os.path.isdir(output):
    os.mkdir(output)

result = get_url(path, url)
img_links = get_img_links(result)

base_url = url  # You can modify this based on your requirements
for index, img_link in enumerate(img_links):
    img_link = img_link["src"]
    print("Downloading...")
    if img_link:
        download_img(img_link, index, base_url)


print("Download Complete!!")
