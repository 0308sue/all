import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')
driver.get('https://gogle.com')

driver.get('https://www.youtube.com/c/paikscuisine/videos')

all_videos = driver.find_elements(By.ID, "dismissible")

body_tag = driver.find_element(By.TAG_NAME, 'body')
# print(body_tag)
body_tag.send_keys(Keys.END)
print(driver.execute_script('return document.documentElement.scrollHeight'))

while True:
    last_height = driver.execute_script(
        'return document.documentElement.scrollHeight')
    # 스크롤 10번
    for i in range(10):
        body_tag.send_keys(Keys.END)
        time.sleep(1)
    new_height = driver.execute_script(
        'return document.documentElement.scrollHeight')
    print('new_height', new_height)

    if last_height == new_height:
        print('화면 길이 같아서 반복종료')
        break
