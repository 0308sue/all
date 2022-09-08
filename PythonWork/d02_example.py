# 1. p.41 1~ 10까지의 합 출력
import random
import re
sum = 0
for i in range(0, 11):
    sum += i
print('합계 : ', sum)


# 2. p.44 구구단 출력
for i in range(1, 10):
    print('[', i, '단]')
    for j in range(1, 10):
        print(i, '*', j, '=', i*j)
    print()


# 3.
exam = "저는 92년에 태어났습니다. 88년에는 올림픽이 있었습니다. 지금은 2022년 입니다."
ret = re.findall(r'\d.+?년', exam)
print(ret)

# 4. .으로 구분하여 문장 출력
d = 'I have a dog. I am not a girl. Yoi are not alone. I am happy'
ret1 = re.split('\.', d)
print(ret1)
ret2 = d.split('.')
print(ret2)

# 5.
txt = "Chandler: Then I look down, and I realize there's a phone... there.Joey: Instead of...?Chandler: That's right.Joey: Never had that dream."

# 등장인물 출력
m = re.findall(r'[A-Z][a-z]+:', txt)
print(m)

# 등장인물 중복 제거
print(set(m))

# 6. p.75 문자열에서 무작위로 5개 문자 추출하여 새로운 변수 pw에 하나씩 병합
pw = str()
chars = '한글 우수'
for _ in range(5):
    pw = pw + random.choice(chars)
print(pw)

# 7. p.83 animal 리스트에서 새가 저장되어 있는 위치(인덱스만) 저장하는 리스트
bird_pos = []
animals = ['새', '코끼리', '강아지', '새', '강아지', '새']

# for i in range(len(animals)):
#     if (animals[i] == '새'):
#         bird_pos.append(i)

for i in enumerate(animals):
    if(animals == '새'):
        bird_pos.append(i)

print('새 위치 : ', bird_pos)

# 8. p.84 mylist에서 짝수만 출력
mylist = [3, 4, 5, 9, 2, 8, 2, 1]
new_list = []
for i in mylist:
    if i % 2 == 0:
        new_list.append(i)
print(new_list)

# 리스트 함축 : for문과 if조건식을 함축적으로 결합한 형식
# i for in 리스트명 if 조건식
new_listw2 = [i for i in mylist if (i % 2) == 0]
print(new_listw2)
