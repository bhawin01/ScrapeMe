from bs4 import BeautifulSoup
import requests


seasonURL = "https://www.stopatnothinggame.com/"

page = requests.get(seasonURL)
soup = BeautifulSoup(page.content, "html.parser")


btn = soup.find_all("button")

for a in btn:
    print(a)