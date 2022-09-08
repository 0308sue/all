import matplotlib as mpl
from matplotlib.pyplot import title
from selenium import webdriver as wd
from bs4 import BeautifulSoup
import re
import pandas as pd
import matplotlib.pyplot as plt

path = 'D:\\chromdriver\\chromedriver_win32\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(path, options=options)
driver.get('https://www.youtube.com/c/paikscuisine/videos')
page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')
all_videos = soup.find_all(id='dismissible')
datas = []

for video in all_videos:
    title = video.find(id='video-title').get_text()
    video_time = video.find(
        'span', {'class': 'style-scope ytd-grid-video-renderer'}).get_text()
    ret = re.findall(r'\d\d*[.]?\d?', video_time)
    print(ret)

    # num = float(ret.pop(0))
    # datas.append([title, num])

# print(datas)
# youtube = pd.DataFrame(datas, columns=('제목', '조회수'))
# youtube.to_csv('youtube.csv', mode='w', encoding='utf-8-sig', index=True)

# dict_youtube = {'100만 이상': 0, '50만 이상': 0, '10만 이상': 0}
# for item in datas:
#     i = item[1]
#     if i >= 100:
#         dict_youtube['100만 이상'] += 1
#     elif i >= 50:
#         dict_youtube['50만 이상'] += 1
#     elif i >= 10:
#         dict_youtube['10만 이상'] += 1


# font_name = mpl.font_manager.FontProperties(
#     fname='C:/Users/admin/Desktop/font/extrabold.ttf').get_name()
# mpl.rc('font', family=font_name)

# figure = plt.figure()
# axes = figure.add_subplot(111)
# axes.pie(dict_youtube.values(), labels=dict_youtube.keys(), autopct='%.1f%%')
# plt.show()
