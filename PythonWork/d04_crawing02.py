from unittest import result
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

# https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=1&sido=&gugun=&store=


# def hollys_store(result):
#     for page in range(1, 6):
#         url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=' % page
#         html = urllib.request.urlopen(url)
#         soup = BeautifulSoup(html, 'html.parser')
#         tbody = soup.find('tbody')

#         for i in tbody.find_all('tr'):
#             store = i.find_all('td')
#             loc = store[0].string
#             name = store[1].string
#             addr = store[3].string
#             phnum = store[-1].string
#             result.append([loc, name, addr, phnum])
#     return

def hollys_store(result):
    for page in range(1, 6):
        url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=' % page
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        tbody = soup.select_one(
            '#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody')

        for i in tbody.select('tr'):
            store = i.select('td')
            loc = store[0].string
            name = store[1].string
            addr = store[3].string
            phnum = store[-1].string
            result.append([loc, name, addr, phnum])
    return


result = []
print('-- Hollys strome crawling >>>>')
hollys_store(result)
holls_tbl = pd.DataFrame(result, columns=(
    'store', 'sido-gu', 'adress', 'phone'))
print(holls_tbl)


#contents > div.content > fieldset > fieldset
