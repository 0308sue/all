from bs4 import BeautifulSoup
import urllib.request


# for page in range(1, 6):
#     url = 'https://movie.daum.net/ranking/reservation'
#     html = urllib.request.urlopen(url)
#     soup = BeautifulSoup(html, 'html.parser')
# ol = soup.find('ol', class_='list_movieranking')
# rank = ol.find_all('div', class_='thumb_cont')
# for i in rank:
#     title = i.find('a', 'link_txt').get_text()
#     stars = i.find('span', 'txt_grade').get_text()
#     ticket = i.find('span', {'class': 'txt_num'}).get_text()
#         print('제목 :', title, end='/ ')
#         print('평점 :', stars, end='/ ')
#         print('예매율 :', ticket)

# url = 'https://movie.daum.net/ranking/reservation'
# html = urllib.request.urlopen(url)
# soup = BeautifulSoup(html, 'html.parser')
# tbody = soup.select_one(
#     '#mainContent > div > div.box_ranking > ol')
# li = tbody.select('li')

# for i in li:
#     title = i.find('a', 'link_txt').get_text()
#     stars = i.find('span', 'txt_grade').get_text()
#     ticket = i.find('span', {'class': 'txt_num'}).get_text()
# print('제목 :', title, end='/ ')
# print('평점 :', stars, end='/ ')
# print('예매율 :', ticket)


url = 'https://movie.daum.net/ranking/reservation'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.select_one(
    '#mainContent > div > div.box_ranking > ol')

for i in tbody.select('li'):
    title = i.select_one('a.link_txt').get_text()
    stars = i.select_one('span.txt_grade').get_text()
    ticket = i.select_one('span.txt_num').get_text()
    print('제목 :', title, end='/ ')
    print('평점 :', stars, end='/ ')
    print('예매율 :', ticket)
