from bs4 import BeautifulSoup
import requests
import re
req = requests.get('https://news.daum.net/digital#1')

html = req.text
soup = BeautifulSoup(html, 'html.parser')

links = soup.select('a[href]')
# eco = soup.select('body > div.container-doc.cont-category > main > section > div.main-sub > div:nth-child(1) > ul')

for t in links:
    if re.search('https://v.\w+', t['href']):  # . 임의의 문자 1개  \w 숫자와 문자
        print(t.get_text().strip())
