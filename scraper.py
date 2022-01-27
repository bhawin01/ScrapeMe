from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import requests


seasonURL = "http://www.espncricinfo.com/ipl/engine/series/313494.html"

page = requests.get(seasonURL)

soup = BeautifulSoup(page.content, "html.parser")
myhref = soup.find_all("a", href=True)
for a in myhref:
    try:
        if "https://www.espncricinfo.com/series/8048/scorecard" in a['href']:
            soup = BeautifulSoup(page.content, "html.parser")

            Usrel = requests.get(a['href'])

            soup = BeautifulSoup(Usrel.content, "html.parser")

            mydivs = soup.find_all("div", class_="match-detail--right")

            myspan = soup.find_all('span', {"data-reactid": True})

            # difference of 5 in data react id

            toss = ""
            for x in range(0, 1000):
                try:
                    price = soup.find('span', attrs={"data-reactid": x})

                    final_toss = price.text
                    for a in final_toss:
                        if "elected" in final_toss:
                            id = x
                            break
                except:
                    pass

            final = soup.find('span', attrs={"data-reactid": id})
            final = final.text
            toss_winner = ""

            for p in final:
                if p == ",":
                    break
                toss_winner = toss_winner + p
            print(toss_winner)








    except:
        pass


