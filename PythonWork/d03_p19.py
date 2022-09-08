from cgitb import html
from bs4 import BeautifulSoup

html = '''
<html><body>
<h1>스크레이핑 이란?</h1>
<p>웹 페이지를 분석하는 것</p>
<p>원하는 부분을 추출하는 것</p>
</html></body>
'''
soup = BeautifulSoup(html, 'html.parser')
print(soup)
h1 = soup.html.body.h1
print(h1)

p = soup.html.body.p
print(p)

p1 = p.next_sibling.next_sibling
print(p1)
print('h1 : ', h1.string)
print('p : ', p.string)
print('p1 : ', p1.string)

html2 = '''
<html><body>
<h1 id='titel'>스크레이핑 이란?</h1>
<p id='body'>웹 페이지를 분석하는 것</p>
<p>원하는 부분을 추출하는 것</p>
</html></body>
'''
soup = BeautifulSoup(html2, 'html.parser')
title = soup.find(id='titel')
print(title)
print('body : ', soup.find(id='body').string)
