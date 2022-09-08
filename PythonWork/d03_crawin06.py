from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

req = requests.get(
    'https://finance.naver.com/')

html = req.text
soup = BeautifulSoup(html, 'html.parser')

links = soup.select(
    '#container > div.aside > div > div.aside_area.aside_popular > table > tbody >tr')

list = []
for i in links:
    name = i.select_one('th > a').getText()
    curr_price = i.select_one('td').getText()
    ch_direction = i.select_one('td > img')['alt']
    ch_price = i.select_one('td > span').get_text().strip()
    list.append([name, curr_price, ch_direction, ch_price])
print(list)

write_wb = Workbook()
write_ws = write_wb.create_sheet('결과')
for data in list:
    write_ws.append(data)

write_wb.save(r'testfinance.xlsx')
