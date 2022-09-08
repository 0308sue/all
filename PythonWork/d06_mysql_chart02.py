from cProfile import label
from unittest import result
from matplotlib import pyplot as plt
import pymysql
import matplotlib as mpl


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

x = []
y = []
y2 = []
for row in Busan:
    x.append(row[0].split('-')[2])
    y.append(row[1])
    y2.append(row[2])

font_name = mpl.font_manager.FontProperties(
    fname='C:/Users/admin/Desktop/font/extrabold.ttf').get_name()
mpl.rc('font', family=font_name)

figure = plt.figure(figsize=(10, 6))
axes = figure.add_subplot(111)
axes.plot(x, y, label='최저기온')
axes.plot(x, y2, label='최고기온')

plt.legend()
plt.show()


Busan2 = "select wf, count(*) from forecast where city='남원' group by wf"
cur.execute(Busan2)
result1 = cur.fetchall()
print(result1)

wfData = []
wfDataCount = []
for r in result1:
    wfData.append(r[0])
    wfDataCount.append(r[1])

plt.bar(wfData, wfDataCount)
plt.show()

plt.pie(wfDataCount, labels=wfData, autopct='%.1f%%')
plt.show()
