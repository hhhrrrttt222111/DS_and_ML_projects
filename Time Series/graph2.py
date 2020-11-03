import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("fremont-bridge.csv", index_col='Date', parse_dates=True)
data.columns = ["West", "East"]
data["Total"] = data["West"] + data["East"]

by_time = data.groupby(data.index.time).mean()
hourly_ticks = 4 * 60 * 60 * np.arange(6)
by_time.plot(xticks= hourly_ticks, style=[':', '--', '-'])
plt.ylabel("Traffic according to time")
plt.show()
