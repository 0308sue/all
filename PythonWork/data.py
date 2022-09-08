import os
import requests

for j in range(1, 7001):
    url = "http://211.237.50.150:7080/openapi/3c0858b38da108da55ef768a23b2ee6e94601f96df0fc4f6dbbeb821cd18fc7c/json/Grid_20220621000000000617_1/2/18?DDLN_DT=%d" % j
    requests_data = requests.get(url)
    if requests_data.status_code != 200:
        print("오류 발생, code :", requests_data.status_code)
    data_basic = requests_data.json()
    print(data_basic)
