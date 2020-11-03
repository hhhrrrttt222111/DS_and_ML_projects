import pandas as pd


births = pd.read_csv("births.csv")
# print(births.head())

births['day'].fillna(0, inplace=True)
births['day'] = births['day'].astype(int)

births['decade'] = 10 * (births['year'] // 10)
births.pivot_table('births', index='decade', columns='gender', aggfunc='sum')
print(births.head())