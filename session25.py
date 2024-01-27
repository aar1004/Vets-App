# WEB SCRAPPING

import requests
from bs4 import BeautifulSoup

url = "https://www.indiatoday.in/sports"
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
# print(type(soup), id(soup))
# print(soup.pretify())

tags = soup.find_all("div", class_="B1")
for tag in tags:
    print("---------------------------")
    print(tag.text)
    print("---------------------------")
    print()
