from bs4 import BeautifulSoup
import requests
import re
req = requests.get(
    'https://www.dhlottery.co.kr/gameResult.do?method=byWin&wiselog=H_C_1_1')

html = req.text
soup = BeautifulSoup(html, 'html.parser')

links = soup.select('#article > div:nth-child(2) > div > div.win_result > div')

for i in links:
    print(i.get_text())

lists = soup.find_all('span', 'ball')

for i in lists:
    print(i.get_text(), end='\t')

#container > div.aside > div > div.aside_area.aside_popular > table > tbody
