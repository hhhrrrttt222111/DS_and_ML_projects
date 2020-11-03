import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

seaborn.set(style="whitegrid")

cities = pd.read_csv("california_cities.csv")
lat, long = cities["latd"], cities["longd"]
pop, area = cities["population_total"], cities["area_total_km2"]

plt.scatter(long, lat, label=None, c=np.log10(pop), cmap='viridis', s=area, linewidth=0, alpha=0.5)
plt.axis('equal')
plt.xlabel('Longitude')
plt.ylabel('Longitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7)


for area in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.3, s=area, label=str(area) + 'km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Areas')
plt.title("Area and Population of California Cities")

plt.show()
