import pandas as pd

df = pd.read_csv('survey.csv', encoding='cp949')
print(df.head())
# 평균
print(df.mean())

# 수입 평균
print('수입 평균 : ', df.income.mean())
# 수입 합계
print('수입 합계 : ', df.income.sum())
# 수입 중앙값
print('수입 중앙값 : ', df.income.median())

# describe()
print(df.describe())
print(df.income.describe())
print(df.sex.value_counts())
