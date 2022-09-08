from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import re


path = 'D:\\chromdriver\\chromedriver_win32\\chromedriver.exe'
driver = wd.Chrome(path)
driver.implicitly_wait(2)
driver.get(
    'https://map.naver.com/v5/?c=14366067.4688943,4184643.8559866,15,0,0,2,dh')
driver.maximize_window()
time.sleep(3)
driver.find_element(By.CLASS_NAME, 'input_search').send_keys('디저트')
driver.find_element(
    By.CSS_SELECTOR, '#container > shrinkable-layout > div > app-base > search-input-box > div > div > button.button_search').click()
# time.sleep(3)
# driver.execute_script('window.scrollTo(0,1000)')
# time.sleep(2)
# driver.find_element(
#     By.CSS_SELECTOR, 'body > div.wrap > div.right_area.is-left > section > div.n-result-all > div > section:nth-child(1) > a').click()
# time.sleep(2)

# search_list = driver.find_element(By.ID, 'searchList')
# li = search_list.find_elements(By.CLASS_NAME, 'li_box')
# itemlist = []


# for i in li:
#     # for td in tr.find_elements(By.TAG_NAME,'td'):
#     info = i.find_element(By.CLASS_NAME, 'article_info')
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
