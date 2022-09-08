from bs4 import BeautifulSoup
import requests
from sympy import beta

req = requests.get('https://news.daum.net/digital#1')

html = req.text
soup = BeautifulSoup(html, 'html.parser')

news = soup.find_all('strong', 'tit_g')

for i in range(len(news)):
    print((i+1), ".", news[i].get_text().strip())
