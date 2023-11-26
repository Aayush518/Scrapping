import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)
# print(r)
soup = BeautifulSoup(r.content, "html.parser")
# print(soup.prettify())

table = soup.find("table", class_="ih-td-tab auction-tbl")
# print(table)
title=table.find_all("th")
# print(title)
header=[]
for i in title:
    name=i.text
    header.append(name)

# print(header)
df= pd.DataFrame(columns=header)
# print(df)
rows=table.find_all("tr")
# print(rows)
for i in rows[1:]:
    first_td=i.find_all("td")[0].find("div",class_="ih-pt-ic").text.strip()
    data=i.find_all("td")[1:]
    # print(data)
    row = [tr.text for tr in data]
    row.insert(0,first_td)
    l=len(df)
    df.loc[l]=row
print(df)

df.to_csv("ipl_auction.csv",index=True)