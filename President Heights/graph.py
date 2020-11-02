import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("heights.csv")
height = np.array(data["height(cm)"])

plt.hist(height)
plt.title("Height Distribution of Presidents of USA")
plt.xlabel("Height")
plt.ylabel("Number")
plt.show()
