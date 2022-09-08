from cgitb import html
from ctypes.wintypes import PINT
from urllib import response
import requests
from yarl import URL

URL = "http://www.naver.com"
response = requests.get(URL)
html_data = response.text
# print(html_data)

print(html_data.find('<h3 class="blind">'))