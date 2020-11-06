import pandas as pd
from matplotlib import pyplot as plt

plt.xkcd()


data = pd.read_csv('./data/scatter.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, edgecolor='black', linewidths=1, alpha=0.75, c=ratio, cmap='summer')
plt.xscale('log')
plt.yscale('log')
cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ration')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()
