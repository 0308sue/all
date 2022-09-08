import csv,re

f = open('popSeoul.csv','r')
reader = csv.reader(f)

output = []
for i in reader:
    tmp = []
    for j in i:
        try:
            if re.search('\d',j):
                tmp.append(float(re.sub(',','',j)))
            else:
                tmp.append(j)
        except:
            pass
    output.append(tmp)

new = [['구','한국인','외국인','외국인 비율(%)']]

for i in output:
    # print(i)
    foreign = 0
    try :
        foreign = round(i[2]/(i[1]+i[2])*100,1)
        # print(foreign)
        if foreign > 5:
            new.append([i[0],i[1],i[2],foreign])
    except:
        pass
print(new)
print(len(new))