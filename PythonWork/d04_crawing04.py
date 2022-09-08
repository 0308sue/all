import pandas as pd
from bs4 import BeautifulSoup
import requests

req = requests.get(
    'https://www.weather.go.kr/weather/observation/currentweather.jsp')

soup = BeautifulSoup(req.text, 'html.parser')

datas = []

tbody = soup.select_one(
    '#weather_table > tbody')
tr = tbody.select('tr')

for i in tr:
    row = i.select('td')
    if len(row) > 0:
        city = row[0].string
        temp = row[5].string
        water = row[-4].string
        print('지역 :', city, end='/ ')
        print('현재 기온 :', temp, end='/ ')
        print('습도 :', water)
        datas.append([city, temp, water])

with open('weather.csv', 'w') as file:
    print('파일저장')
    file.write('point,temp,hum\n')
    for item in datas:
        row = ','.join(item)
        file.write(row+'\n')


df = pd.read_csv('weather.csv', index_col='point', encoding='euc-kr')
print(df)
