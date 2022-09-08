import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl

df = pd.read_csv('weather.csv', index_col='point', encoding='euc-kr')
# print(df)
city_df = df.loc[['서울', '대전', '대구', '광주', '부산']]
print(city_df)

font_name = mpl.font_manager.FontProperties(
    fname='C:/Users/admin/Desktop/font/extrabold.ttf').get_name()
mpl.rc('font', family=font_name)

ax = city_df.plot(kind='bar', title='날씨', figsize=(
    12, 7), legend=True, fontsize=12)
ax.set_xlabel('도시', fontsize=12)
ax.set_ylabel('기온/습도', fontsize=12)
ax.legend(['기온', '습도'], fontsize=12)
plt.show()
