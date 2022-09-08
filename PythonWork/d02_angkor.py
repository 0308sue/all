from posixpath import split
import re

from numpy import size

English = 'She is a vegetarian. '
English += 'She does not eat meat.'
English += 'She thinks that animals should not be killed. '
English += 'It is hard for her to hang out with people. '
English += 'Many people like to eat meat. '
English += 'She told his parents not to have meat. '
English += 'They laughed at her. She realized they couldn\'t give up meat.'

Korean = '그녀는 채식주의자입니다.'
Korean += '그녀는 고기를 먹지 않습니다. '
Korean += '그녀는 동물을 죽이지 말아야한다고 생각합니다. '
Korean += '그녀가 사람들과 어울리는 것은 어렵습니다. '
Korean += '많은 사람들이 고기를 좋아합니다. '
Korean += '그녀는 부모에게 고기를 먹지 말라고 말했습니다. '
Korean += '그들은 그녀를 비웃었다.'
Korean += '그녀는 그들이 고기를 포기할 수 없다는 것을 깨달았습니다.'

print(English)
print(Korean)

Korean_list = re.split('\.', Korean)
print(Korean_list)
English_list = re.split('\.', English)
print(English_list)

total = []

for i in range(len(Korean_list)):
    total.append([Korean_list[i], English_list[i]])

print(total)

ek = []
for e, k in zip(English.split('.'), Korean.split('.')):
    ek.append([e, k])
print(ek)


total = ['종로구', '151,767', '11,093', '27,394']
# 1. ,제거하고 total 출력 단, 숫자는 정수형으로 표현

for i in total:
    if re.search(',', i):
        total[total.index(i)] = int(re.sub(',', '', i))
print(total)


pop = [['종로구', 151767.0], ['중구', 126409.0], [
    '용산구', 228830.0], ['광진구', 352692.0], ['동대문구', 346551.0]]
# 2. 30만명보다 인구가 적은 지역의 이름을 출력
tmp = []
for i in pop:
    if i[1] < 300000:
        tmp.append(i[0])
print(tmp)
