import email
import re,codecs

from numpy import character
from regex import E

f = codecs.open('friends101.txt',"r",encoding='utf-8')
script101 = f.read()

print(script101[:100])
Line = re.findall(r'Monica:.+',script101)
print(Line[:3])
print(type(Line))

All = re.findall(r'All:.+',script101)
print(All)
print(All[-1])
print(len(All))

char = re.compile(r'[A-Z][a-z]+:')
print(re.findall(char,script101))

a=[1,2,3,4,5,2,2]
print(a)
print(set(a))
y=set(re.findall(char,script101))
print(type(y))
z = list(y)
print(type(z))
character = []

for i in z:
    character += [i[:-1]]
print(character)

character2 = []
for i in z:
    character2 = re.sub(':','',i)
print(character2,end=' ')

print()
txt =  re.findall(r'\([A-Za-z].+[a-z|\/]\)',script101)[:6]
print(txt)

ch = 'Scene:'
ch = re.sub(':','',ch)
print('\n',ch)


a = '제 이메일 주소는 grerate@naver.com'
a += ' 오늘은 today@naver.com 내일은 apple@gmail.com life@abc.co.kr 라는 메일을 사용합니다.'
print(a)

print(re.findall(r'[a-z]+@[a-z.]+',a))

words = ['apple','cat','brave','drama','asise','blow','coat','above']
mm = []
for i in words:
   mm += re.findall(r'a[a-z]+',i)
print("~~~~",mm)

for i in words:
    m = re.search(r'a[a-z]+',i)
    if m:
        print(m.group())
print()

for i in words:
    m = re.match(r'a[a-z]+',i)
    if m:
        print(m.group())
print()

for i in words:
    m = re.match(r'a\d+',i) #\d(숫자) \D(숫자 아닌)
    if m:
        print(m.group())
print()