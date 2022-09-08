from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import re


path = 'D:\\chromdriver\\chromedriver_win32\\chromedriver.exe'
driver = wd.Chrome(path)
driver.implicitly_wait(2)
driver.get(
    'https://www.google.co.kr/maps/?hl=ko')
driver.maximize_window()
time.sleep(3)

driver.find_element(By.ID, 'searchboxinput').send_keys('디저트')
driver.find_element(By.ID, 'searchbox-searchbutton').click()
time.sleep(2)
li = driver.find_elements(
    By.CSS_SELECTOR, '#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd > div').click()
time.sleep(2)

# search_list = driver.find_element(By.ID, 'searchList')
# li = search_list.find_elements(By.CLASS_NAME, 'li_box')
# itemlist = []


for i in li:
    print(i)
    # for td in tr.find_elements(By.TAG_NAME,'td'):
    # info = i.find_element(By.CLASS_NAME, 'article_info')
#     brand = info.find_element(By.CSS_SELECTOR, 'p.item_title > a').text
#     name = info.find_element(By.CLASS_NAME, 'list_info').find_element(
#         By.TAG_NAME, 'a').text
#     price = info.find_element(By.CLASS_NAME, 'price').text
#     price = price.split(' ')
#     if (len(price) == 1):
#         price = price[0]
#     else:
#         price = price[1]

#     review = info.find_element(By.CLASS_NAME, 'count').text
#     itemlist.append([brand, name, re.sub(
#         ',', '', price), re.sub(',', '', review)])

# print(itemlist)

# with open('musinsa.csv', 'w', encoding='utf-8-sig') as file:
#     file.write('브랜드, 제품명, 가격, 리뷰개수\n')
#     for item in itemlist:
#         row = ','.join(item)
#         file.write(row+"\n")
