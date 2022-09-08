import csv
import re


def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)

    return output


total = opencsv('popSeoul2.csv')

for i in total[:5]:
    print(i)

for i in total[:5]:
    for j in i:
        # print(i.index(j)) #위치 확인
        try:
            i[i.index(j)] = float(re.sub(',', '', j))
        except:
            pass
# print(total[:5])

test = [1, 2, 3, 4, 5]
print(test.index(5))

j = '124,586,356'
print(int(re.sub(',', '', j)))
print(float(re.sub(',', '', j)))
