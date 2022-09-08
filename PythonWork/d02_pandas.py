import pandas as pd

df = pd.read_csv('apt_201910.csv', encoding='cp949', thousands=',')
print(len(df))
print(df.shape)
print(df.head())
print(df.tail())
print('------------')
# 면적이 130보다 큰것
print(df[df.면적 > 130])
print('------------')
print(df.loc[:10, ['단지명', '가격']])
print(df.loc[:, ['단지명', '가격', '면적']][df.면적 > 130])

# 지역에 강릉이 들어간 자료만 출력
local_area = df[df.시군구.str.find('강릉') > -1]
print(local_area)

# 지역이 강릉인 지역,가격,단가 10행 출력
print(local_area.loc[:10, ['시군구', '가격', '면적']])

print(df['가격'].head())

# 면적이 130 넘는 아파트의 가격 출력
print(df.가격[df.면적 > 130])

# 면적이 130이 넘고 가격이 2억 미만이 아파트의 가격 출력
print(df.가격[(df.면적 > 130) & (df.가격 < 20000)])

# 면적이 130이 넘거나 가격이 2억 미만이 아파트의 가격 출력
print(df.가격[(df.면적 > 130) | (df.가격 < 20000)])

dfAsc = df.sort_values(by='가격', ascending=True)
print(dfAsc.가격)

print('-'*100)
# 6억원을 초과하는 가격으로 거래된 아파트,가격만 출력
print(df.가격[df.가격 > 60000])

print('-'*100)
# 6억원을 초과하는 가격으로 거래된 아파트,가격 출력
print(df.loc[:, ['가격', '단지명']][df.가격 > 60000])

# 없는 컬럼 생성시에는 df['단가'] 대괄호 무조건 사용 df.단가(불가)
df['단가'] = df.가격/df.면적
print(df.loc[:10, ('시군구', '면적', '단가')])
