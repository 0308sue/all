from cmath import sin
import matplotlib as mpl
from matplotlib.pyplot import title
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re

path = 'D:\\chromdriver\\chromedriver_win32\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(path, options=options)
# print(driver)
driver.get('https://www.melon.com/chart/index.htm')
page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')
# print(soup)
tdoby = soup.select_one('#frm > div > table > tbody')
trs = tdoby.select('tr#lst50')

datas = []

for tr in trs:
    rank = tr.select_one('span.rank').get_text()
    name = tr.select_one('div.ellipsis.rank01>span>a').get_text()
    singer = tr.select_one('div.ellipsis.rank02>a').get_text()
    album = tr.select_one('div.rank03 > a').get_text()
    like = tr.select_one(
        '#lst50 > td:nth-child(8) > div > button > span.cnt').get_text()
    # print(like)
    ret = re.sub('\n총건수\n', '', like)
    ret = re.sub(',', '', ret)
    # lst50 > td:nth-child(8) > div > button > span.cnt > span

#     datas.append([rank, name, singer, album, ret])

# print(datas)

# with open('melon.csv', 'w', encoding='utf-8-sig') as file:
#     file.write('순위 곡명 가수 앨범 좋아요\n')
#     for item in datas:
#         row = ','.join(item)
#         file.write(row+"\n")
