from sympy import im


import usecsv

total = usecsv.opencsv('popSeoul.csv')

newlist = usecsv.switchcsv(total)
print(newlist[:4])

new = [['구', '한국인', '외국인', '외국인 비율(%)']]

for i in newlist:
    # print(i)
    foreign = 0
    try:
        foreign = round(i[2]/(i[1]+i[2])*100, 1)
        # print(foreign)
        if foreign > 5:
            new.append([i[0], i[1], i[2], foreign])
    except:
        pass
print(new)
