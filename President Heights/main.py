import pandas as pd
import numpy as np


data = pd.read_csv("heights.csv")
# print(data.head())

height = np.array(data["height(cm)"])
# print(height)

print("Mean : ", height.mean())
print("Standard Deviation : ", height.std())
print("Minimum : ", height.min())
print("Maximum : ", height.max())

print("25th percentile : ", np.percentile(height, 25))
print("Median : ", np.median(height))
print("75th percentile : ", np.percentile(height, 75))

