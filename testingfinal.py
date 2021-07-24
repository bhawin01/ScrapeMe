from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import requests


page = requests.get("https://www.espncricinfo.com/series/8048/scorecard/597999/royal-challengers-bangalore-vs-mumbai-indians-2nd-match-indian-premier-league-2013")
page
page.status_code



soup = BeautifulSoup(page.content, "html.parser")


mydivs = soup.find_all("div", class_="match-detail--right")


myspan = soup.find_all('span',  {"data-reactid": True})

# difference of 5 in data react id

toss = ""
for x in range(665,667):
    try:
        price = soup.find('span', attrs={"data-reactid": x})
        print(price.text)

        final_toss = price.text
        for a in final_toss:
            if "elected" in final_toss:
                id = x
                break
    except:
        pass


price = soup.find('span', attrs={"data-reactid": id})



print(toss)