import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

driver = webdriver.Chrome('chromedriver')
driver.get('https://gogle.com')
# r = driver.execute_script('return 100*50')
# print(r)

driver.get('https://www.youtube.com/c/paikscuisine/videos')

all_videos = driver.find_elements(By.ID, "dismissible")

datas = []
time.sleep(2)

for video in all_videos:
    title = video.find_element(By.ID, "video-title").text
    clicknums = video.find_element(
        By.CSS_SELECTOR, "span.ytd-grid-video-renderer").text
    # print('제목 :', title)
    # print('조회수 :', clicknums)
    # ret = re.findall(r'\d[.]?\d', clicknums)
    # num = float(ret.pop(0))
    datas.append([title, clicknums])

print(datas)
