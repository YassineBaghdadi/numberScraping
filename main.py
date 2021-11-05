import requests, pandas as pd, os, json, selenium
from bs4 import BeautifulSoup
from lxml import html

# link = "https://www.tripadvisor.com/Restaurants-g187070-France.html"
baseLink = "https://www.yelp.com"
link = "https://www.yelp.com/search?cflt={}&find_loc=France"

page = BeautifulSoup(requests.get(link, timeout=10).content, 'html.parser')
links = [a['href'] for a in page.find_all("a", class_="css-iyhg3f", href=True)]
# for i in links:
#     if i != "http://databyacxiom.com":
#         print(f"{baseLink}{i}")

page = BeautifulSoup(requests.get(f"https://www.yelp.com/biz/le-comptoir-de-la-gastronomie-paris?hrid=mlUbR2SegVd4j6Q9gsHhFA", timeout=10).content, 'html.parser')
phoneNum = page.find_all("p", class_="css-1h1j0y3")
name = page.find("h1", class_="css-yin5a8").text

zipCode = page.find_all("span", class_="raw__373c0__tQAx6")
# [print(i.text) for i in phoneNum]
phone = str(phoneNum[-2].text).replace(" ", "")
print(phone)
print(name)
[print(i) for i in zipCode]

# pageCounter = int(page.find("div", class_="border-color--default__09f24__3Epto text-align--center__09f24__2qZj2").find("span", class_="css-e81eai").text.split(" of ")[1])*10


# def searchByNiche(niche):
#     for start in range(0, pageCounter, 10):
#         page = BeautifulSoup(requests.get(f"{link.format(niche)}&start={start}", timeout=10).content, 'html.parser')
#         links = [a['href'] for a in page.find_all("a", class_="css-iyhg3f", href=True)]
#         for item in links:
#             theItem = BeautifulSoup(requests.get(f"{baseLink}{i}", timeout=10).content, 'html.parser')
#