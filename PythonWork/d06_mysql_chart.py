from unittest import result
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import pymysql
from cgitb import html
import requests
import matplotlib as mpl

dbURL = '127.0.0.1'
dbPort = 3306
dbUser = 'root'
dbPass = 'root'

conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser,
                       passwd=dbPass, db='bigdb', charset='utf8', use_unicode=True)

req = requests.get('https://movie.daum.net/ranking/reservation')
html = req.text
soup = BeautifulSoup(html, 'lxml')


select_data = 'select grade from `daum_movie` order by grade'
cur = conn.cursor()
cur.execute(select_data)
gradec = cur.fetchall()
# print(gradec)

moviedict = {'9점이상': 0, '8점이상': 0, '7점이상': 0, '6점이상': 0, '5점이상': 0}

for row in gradec:
    a = float(row[0])
    if a >= 9:
        moviedict['9점이상'] += 1
    elif a >= 8:
        moviedict['8점이상'] += 1
    elif a >= 7:
        moviedict['7점이상'] += 1
    elif a >= 6:
        moviedict['6점이상'] += 1
    elif a >= 5:
        moviedict['5점이상'] += 1


font_name = mpl.font_manager.FontProperties(
    fname='C:/Users/admin/Desktop/font/extrabold.ttf').get_name()
mpl.rc('font', family=font_name)

figure = plt.figure()
axes = figure.add_subplot(111)
axes.pie(moviedict.values(), labels=moviedict.keys(), autopct='%.1f%%')
plt.show()
