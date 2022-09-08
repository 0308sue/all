from traceback import print_tb
import pandas as pd

data = {
    'year': [2018, 2019, 2020, 2021, 2022],
    'sales': [350, 400, 1050, 2000, 1000]
}

df = pd.DataFrame(data)
print(df)
print(type(df))
print('-'*100)

df2 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]],
                   index=['중간고사', '기말고사'],
                   columns=['1반', '2반', '3반'])
print(df2)

df3 = pd.DataFrame([[20201101, 'Kim', 60, 55], [20201101, 'Lee', 90, 95], [
                   20201101, 'Hong', 70, 75], [20201101, 'Park', 40, 55]], columns=['학번', '이름', '중간고사', '기말고사'])
print(df3)
print(df3.sum())
print(df3.mean())

df4 = pd.DataFrame([[20201101, 'Kim', 90, 95], [20201101, 'Lee', 90, 95], [
                   20201101, 'Hong', 90, 95], [20201101, 'Park', 90, 95]])
print(df4)
df4.columns = ['학번', '이름', '중간고사', '기말고사']
print(df4)
print(df4.tail())

df3.to_csv('pandas03.csv', header='False')
df5 = pd.read_csv('pandas03.csv', encoding='utf-8')
print(df5)
