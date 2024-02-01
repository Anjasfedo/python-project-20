import requests

from bs4 import BeautifulSoup

url = "https://www.codewithtomi.com/"

r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

titles = soup.find_all("h2", {"class": "post-title"})

for title in titles:
    print(title.getText())
