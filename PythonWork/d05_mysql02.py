from cgitb import html
from unittest import result
import requests
import pymysql
from bs4 import BeautifulSoup


dbURL = '127.0.0.1'
dbPort = 3306
dbUser = 'root'
dbPass = 'root'

conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser,
                       passwd=dbPass, db='bigdb', charset='utf8', use_unicode=True)

Busan = "select tmef,tmn,tmx from forecast where city = '부산'"
cur = conn.cursor()
cur.execute(Busan)

Busan = cur.fetchall()

datas = []
for row in result:
    datas.append([row[2], row[4], row[5]])

print(datas)
