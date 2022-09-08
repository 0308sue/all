import encodings
import urllib.request
import requests
from bs4 import BeautifulSoup

data = []
datas = []
for menu in range(1, 4):
    url = 'https://www.nielsenkorea.co.kr/tv_terrestrial_day.asp?menu=Tit_1&sub_menu=%d_2&area=00&begin_date=202207' % menu
    html = requests.get(url)

    soup = BeautifulSoup(html.content, 'html.parser')

    tr = soup.select(
        '#sub_body > table:nth-child(4) > td >table > tr')
    data+menu
    for i in tr[3:13]:

        rank = i.select_one('td.tb_txt_center').get_text().replace('\t', '')
        channel = i.select_one(
            'td:nth-child(2)').get_text().replace('\r\n', '').strip()
        title = i.select_one('td.tb_txt').get_text().replace('\t', '')
        percent = i.select_one(
            'td:nth-child(4)').get_text().replace('\r\n', '').strip()
        data.append([rank, channel, title, percent])
datas.append(data)
print(datas)
