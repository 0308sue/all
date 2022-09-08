from bs4 import BeautifulSoup
import requests
import re
req = requests.get('https://finance.daum.net/')

html = req.text
soup = BeautifulSoup(html, 'html.parser')

links = soup.select('#boxIndexTabs > ul >li')
print(links)

for i in links:
    print(i.select_one('a').get_text())

for i in range(len(links)):
    print((i+1), ".", links[i].get_text().strip())

for i, link in enumerate(links):
    print((i+1), ".", link.get_text().strip())

links2 = soup.select('#boxIndexTabs > ul >li a')
print(links2)

for i in links2:
    print(i.get_text())
