from bs4 import BeautifulSoup
import pymysql
from cgitb import html
import requests

dbURL = '127.0.0.1'
dbPort = 3306
dbUser = 'root'
dbPass = 'root'

conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser,
                       passwd=dbPass, db='bigdb', charset='utf8', use_unicode=True)

insert_movie = 'insert into `daum_movie`(`title`,`grade`,`reserve`) values(%s,%s,%s)'

req = requests.get('https://movie.daum.net/ranking/reservation')
html = req.text
soup = BeautifulSoup(html, 'lxml')

select_data = 'select tmef from `daum_movie` order by title desc limit 1'
cur = conn.cursor()
cur.execute(select_data)

titlec = cur.fetchone()

movie = []
ol = soup.find('ol', class_='list_movieranking')
rank = ol.find_all('li')
# print(rank)
# for i in rank:
#         title = i.find('a', 'link_txt').get_text()
#         grade = i.find('span', 'txt_grade').get_text()
#         reserve = i.find('span', {'class': 'txt_num'}).get_text()
#         movie.append([title, grade, reserve])

# print(movie)

# for i in movie:
#     cur = conn.cursor()
#     cur.execute(insert_movie, (i[0], i[1], i[2]))
#     conn.commit()

cur = conn.cursor()

for i in rank:
    title = i.find('a', 'link_txt').get_text()
    grade = i.find('span', 'txt_grade').get_text()
    reserve = i.find('span', {'class': 'txt_num'}).get_text()
    cur.execute(insert_movie, (title, grade, reserve))
    conn.commit()
