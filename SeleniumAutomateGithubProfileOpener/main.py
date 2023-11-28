from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import chrome
from selenium.webdriver.common.keys import Keys
import time

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)



path="/usr/local/bin/chromedriver"
s=Service(path)
driver=webdriver.Chrome(options=options,service=s)
driver.get("https://www.google.com/")
time.sleep(2)
box=driver.find_element("xpath","/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
box.send_keys("Github profile Aayush518")
box.send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element("xpath","""//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a""").click()
time.sleep(2)
driver.save_screenshot("screenshot.png")
time.sleep(2)