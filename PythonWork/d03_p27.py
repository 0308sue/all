from bs4 import BeautifulSoup
import urllib.request as req

url = 'https://finance.naver.com/marketindex/'
res = req.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')
#exchangeList > li.on > a.head.usd > div > span.blind
txt = soup.select_one('#exchangeList > li.on > a.head.usd > div')
print(txt)
txt1 = soup.select('div.head_info > span')
print(txt1)
print('///////:', txt.select('span')[0].string)

txt2 = txt.select('span')
print(txt2)

for sp in txt2:
    print(sp.string)

price = soup.select_one('div.head_info > span.value').string
print('price : ', price)

updown = soup.select_one('div.head_info > span.blind').string
print('updown : ', updown)
