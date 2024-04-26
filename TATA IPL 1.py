
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction/2023"
r = requests.get(url)
#print(r)


soup = BeautifulSoup(r.text,"lxml")
print(soup)


table = soup.find("table", class_ = "st-table statsTable ng-scope")
#print(table)
title = soup.find_all("th")
print(title)

header = []
for i in title:
    name = i.text
    header.append(name)

#print(header)

df = pd.DataFrame(columns=header)
#print(df)

rows = soup.find_all("tr")
print(rows)

#td_elements = soup.find_all_("td")

#if 'td_elements':

div_elements = i.find_all("div", class_="(np-leaderInnserSectionBg col-100 floatLft flexDisplay justifyCenter textCenter")

if div_elements:
    first_td = div_elements[0].text.strip()
    # Continue with the rest of your code
else:
    # Handle the case when no "div" elements are found
#for i in rows[1:]:
    #first_td = i.find_all("div", class_="(key,list) in tourBattingStats | filter:playerNameSearch | limitTo:statsListLimit").text.strip()
    data = i.find_all("td")[1:]
    print(data)
    row = [soup.text for soup in data]
    print(row)
    row.insert(0, 'first_td')
    l = len(df)
    df.loc[l] = 'row'


print(df)
df.to_csv("ipl Auction stats.xlsx")