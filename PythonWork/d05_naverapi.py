import datetime
import urllib.request
import json

from sympy import total_degree


clientId = 'NrPNPDW61voksnLYBOQl'
clientSecrete = '8VppI02qre'


def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', clientId)
    req.add_header('X-Naver-Client-Secret', clientSecrete)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            # print('[%s] Url Request Success' % datetime.datetime.now())
            return response.read().decode('utf-8')
    except:
        return None


def getNaverSearch(node, srcText, start, display):
    base = 'https://openapi.naver.com/v1/search'
    node = '/news.json'
    parameters = '?query=%s&start=%s&display=%s' % (
        urllib.parse.quote(srcText), start, display)
    url = base+node+parameters
    responseDecode = getRequestUrl(url)
    # print(responseDecode)
    if responseDecode == None:
        return None
    else:
        return json.loads(responseDecode)  # load() : JSON 문자열을 Python 객체로
    return None


def getPostData(post, jsonResult, cnt):
    title = post['title']
    originallink = post['originallink']
    link = post['link']
    description = post['description']
    pubDate = post['pubDate']
    format = '%a, %d %b %Y %X %z'
    pubDate = datetime.datetime.strptime(pubDate, format)
    pubDate = pubDate.strftime("%Y%m%d")
    pubDate = str(pubDate)

    jsonResult.append({'cnt': cnt, 'title': title, 'description': description,
                      'originallink': originallink, 'link': link, 'pubDate': pubDate})
    # jsonResult.append(description)


node = 'news'
srcText = '돼지고기'
cnt = 0
jsonResult = []

jsonResponse = getNaverSearch(node, srcText, 1, 100)
total = jsonResponse['total']

while((jsonResponse != None) and (jsonResponse['display'] != 0)):
    for post in jsonResponse['items']:
        cnt += 1
        getPostData(post, jsonResult, cnt)
    start = jsonResponse['start']+jsonResponse['display']
    jsonResponse = getNaverSearch(node, srcText, start, 10)

print('전체 검색: %d 건' % total)

with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='utf-8-sig') as outfile:
    jsonFile = json.dumps(jsonResult, indent=4,
                          sort_keys=True, ensure_ascii=False)
    outfile.write(jsonFile)
