import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set()

births = pd.read_csv("births.csv")
births['decade'] = 10 * (births['year'] // 10)
births.pivot_table('births', index='decade', columns='gender', aggfunc='sum')
birth_decade = births.pivot_table('births', index='decade', columns='gender', aggfunc='sum')
birth_decade.plot()
plt.ylabel("Total births per year")
plt.show()


