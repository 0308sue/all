from bs4 import BeautifulSoup
import requests

codes = ['252670', '251340']
prices = []

for code in codes:
    url = 'https://finance.naver.com/item/main.naver?code='+code
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    today = soup.select_one('#chart_area>div.rate_info > div > p.no_today')
    title = soup.select_one('#middle > div.h_company > div.wrap_company > h2')
    price = today.select_one('span.blind')
    prices.append(title.get_text())
    prices.append(price.get_text())

print(prices)
