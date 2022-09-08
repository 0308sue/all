from collections import Counter
from email import header
from bs4 import BeautifulSoup
import urllib.request
from matplotlib import font_manager, pyplot as plt, rc
import pymysql
import os
from pandas import DataFrame
import folium
import requests
import re
from konlpy.tag import Okt
from sympy import rotations
from wordcloud import WordCloud
from myPro02.settings import TEMPLATE_DIR, STATIC_DIR


def melon_crawing(datas):
    header = {'User-Agent': 'Mozilla/5.0'}
    req = requests.get('https://www.melon.com/chart/index.htm', headers=header)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    tdoby = soup.select_one('#frm > div > table > tbody')
    trs = tdoby.select('tr#lst50')

    for tr in trs[:10]:
        rank = tr.select_one('span.rank').get_text()
        name = tr.select_one('div.ellipsis.rank01>span>a').get_text()
        singer = tr.select_one('div.ellipsis.rank02>a').get_text()
        album = tr.select_one('div.rank03 > a').get_text()
        like = tr.select_one(
            '#lst50 > td:nth-child(8) > div > button > span.cnt').get_text()
        like = re.sub('\n총건수\n', '', like)
        like = re.sub(',', '', like)

        tmp = dict()
        tmp['rank'] = rank
        tmp['name'] = name
        tmp['singer'] = singer
        tmp['album'] = album
        tmp['like'] = like
        datas.append(tmp)


def make_wordCloud(data):
    message = ''
    for item in data:
        if 'message' in item.keys():
            message = message+re.sub(r'[^\w]', ' ', item['message'])
    nlp = Okt()
    message_N = nlp.nouns(message)
    count = Counter(message_N)
    word_count = dict()
    for tag, counts in count.most_common(80):
        if(len(str(tag)) > 1):
            word_count[tag] = counts
            print("%s : %d" % (tag, counts))

    font_path = 'C:/Users/admin/Desktop/font/extrabold.ttf'
    wc = WordCloud(font_path, background_color='ivory', width=800, height=600)
    cloud = wc.generate_from_frequencies(word_count)
    plt.figure(figsize=(8, 8))
    plt.imshow(cloud)
    plt.axis('off')
    cloud.to_file('./static/images/k_wordCloud.png')


def weater_crawling(last_date, weather):
    req = requests.get(
        'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    for i in soup.find_all('location'):
        weather[i.find('city').text] = []
        for j in i.find_all('data'):
            temp = []
            if (len(last_date) == 0) or (j.find('tmef').text > last_date[0]['tmef']):
                temp.append(j.find('tmef').text)
                temp.append(j.find('wf').text)
                temp.append(j.find('tmn').text)
                temp.append(j.find('tmx').text)
                weather[i.find('city').string].append(temp)
    print(weather)


def weather_make_chart(result, wfs, dcounts):
    font_location = 'C:/Users/admin/Desktop/font/extrabold.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)

    high = []
    low = []
    xdata = []

    for row in result.values_list():
        high.append(row[5])
        low.append(row[4])
        xdata.append(row[2].split('-')[2])
    print(xdata)
    plt.cla()
    plt.figure(figsize=(10, 6))
    plt.plot(xdata, low, label='최저기온')
    plt.plot(xdata, high, label='최고기온')
    plt.legend()
    plt.savefig(os.path.join(
        STATIC_DIR, 'images/weather_busan.png'), dpi=300)

    plt.cla()
    plt.bar(wfs, dcounts)
    plt.savefig(os.path.join(
        STATIC_DIR, 'images/weather_bar.png'), dpi=300)

    plt.cla()
    plt.pie(dcounts, labels=wfs, autopct='%.1f%%')
    plt.savefig(os.path.join(
        STATIC_DIR, 'images/weather_pie.png'), dpi=300)

    image_dic = {'plot': 'weather_busan.png',
                 'bar': 'weather_bar.png', 'pie': 'weather_pie.png'}
    return image_dic


def movie_crawling(data):
    for page in range(1, 11):
        url = 'https://movie.naver.com/movie/point/af/list.naver?&page=%d' % page
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        tbody = soup.select_one(
            '#old_content > table > colgroup> tbody')
        for i in tbody.select('tr'):
            movie = i.select_one('td.title')
            title = movie.select_one('a.movie.color_b').get_text()
            star = movie.select_one('div > em').get_text()
            content_arr = movie.get_text().replace('신고', '').split('\n\n')
            content = content_arr[2].replace('\t', '').replace('\n', '')
            data.append([title, star, content])
            print(data)


def make_chart(titles, points):
    font_location = 'C:/Users/admin/Desktop/font/extrabold.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    plt.cla()
    plt.ylabel('영화평점평균')
    plt.xlabel('영화제목', fontsize=12)
    plt.bar(range(len(titles)), points, align='center')
    plt.xticks(range(len(titles)), list(titles), rotation=20, fontsize=5)
    plt.savefig(os.path.join(STATIC_DIR, 'images\\movie_fig.png'), dpi=300)


def map():
    ex = {'경도': [127.061026, 127.047883, 127.899220, 128.980455, 127.104071, 127.102490, 127.088387, 126.809957, 127.010861, 126.836078, 127.014217, 126.886859, 127.031702, 126.880898, 127.028726, 126.897710, 126.910288, 127.043189, 127.071184, 127.076812, 127.045022, 126.982419, 126.840285, 127.115873, 126.885320, 127.078464, 127.057100, 127.020945, 129.068324, 129.059574, 126.927655, 127.034302, 129.106330, 126.980242, 126.945099, 129.034599, 127.054649, 127.019556, 127.053198, 127.031005, 127.058560, 127.078519, 127.056141, 129.034605, 126.888485, 129.070117, 127.057746, 126.929288, 127.054163, 129.060972],
          '위도': [37.493922, 37.505675, 37.471711, 35.159774, 37.500249, 37.515149, 37.549245, 37.562013, 37.552153, 37.538927, 37.492388, 37.480390, 37.588485, 37.504067, 37.608392, 37.503693, 37.579029, 37.580073, 37.552103, 37.545461, 37.580196, 37.562274, 37.535419, 37.527477, 37.526139, 37.648247, 37.512939, 37.517574, 35.202902, 35.144776, 37.499229, 35.150069, 35.141176, 37.479403, 37.512569, 35.123196, 37.546718, 37.553668, 37.488742, 37.493653, 37.498462, 37.556602, 37.544180, 35.111532, 37.508058, 35.085777, 37.546103, 37.483899, 37.489299, 35.143421],
          '구분': ['음식', '음식', '음식', '음식', '생활서비스', '음식', '음식', '음식', '음식', '음식', '음식', '음식', '음식', '음식', '음식', '음식', '음식', '소매', '음식', '음식', '음식', '음식', '소매', '음식', '소매', '음식', '음식', '음식', '음식', '음식', '음식', '음식', '음식', '음식', '음식', '소매', '음식', '음식', '의료', '음식', '음식', '음식', '소매', '음식', '음식', '음식', '음식', '음식', '음식', '음식']}

    ex = DataFrame(ex)
    lat = ex['위도'].mean()
    long = ex['경도'].mean()
    m = folium.Map([lat, long], zoom_start=9)
    for i in ex.index:
        sub_lat = ex.loc[i, '위도']
        sub_long = ex.loc[i, '경도']
        title = ex.loc[i, '구분']

        folium.Marker([sub_lat, sub_long], tooltip=title).add_to(m)
        m.save(os.path.join(TEMPLATE_DIR, 'bigdata/maptest.html'))


def program_crawling(p):
    url = 'https://www.nielsenkorea.co.kr/tv_terrestrial_day.asp?menu=Tit_1&sub_menu=%d_2&area=00&begin_date=202207' % p
    html = requests.get(url)

    soup = BeautifulSoup(html.content, 'html.parser')

    tr = soup.select(
        '#sub_body > table:nth-child(4) > td >table > tr')
    titles = []
    percents = []
    # sub_body > table:nth-child(4) > tbody > tr:nth-child(1)
    channel = soup.select_one(
        '#Sub1 > div.subbody_tit > span.subbody_tit_kor').get_text()
    year = soup.select_one(
        '#sub_body > table:nth-child(4) >tr:nth-child(1) > td>span').get_text()
    print(channel)
    print(year)
    for i in tr[3:13]:
        title = i.select_one('td.tb_txt').get_text().replace('\t', '')
        percent = i.select_one(
            'td:nth-child(4)').get_text().replace('\r\n', '').strip()
        titles.append(title)
        percents.append(float(percent))

    font_location = 'C:/Users/admin/Desktop/font/extrabold.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)
    plt.cla()
    plt.title(channel+'('+year+')')
    plt.ylabel('시청률')
    plt.bar(titles, percents)
    plt.xticks(rotation=30, fontsize=5)
    plt.savefig(os.path.join(
        STATIC_DIR, 'images\\program'+str(p)+'.png'), dpi=300)
