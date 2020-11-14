import matplotlib.pyplot as plt
import numpy as np


plt.style.use('seaborn-whitegrid')

x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)

# plt.errorbar(x, y, yerr=dy, fmt='.k')
plt.errorbar(x, y, yerr=dy, fmt='o', color='black', ecolor='lightgray', elinewidth=3, capsize=0)
plt.show()
