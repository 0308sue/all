import pandas as pd
import numpy as np
import usecsv


def switchcsv(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(j)
            except:
                pass
    return listName


quest = np.array(switchcsv(usecsv.opencsv('quest.csv')))
print(quest)
print(quest > 5)
quest = 5
print(quest)
print('-----------------')

f = pd.read_csv('quest.csv', encoding='cp949')
quest = np.array(f)
print(quest)

print(quest > 5)
quest[quest > 5] = 100
print(quest)
