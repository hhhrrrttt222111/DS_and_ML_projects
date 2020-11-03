import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("fremont-bridge.csv", index_col='Date', parse_dates=True)
data.columns = ["West", "East"]
data["Total"] = data["West"] + data["East"]

sns.set(style="whitegrid")
data.plot()
plt.ylabel("Hourly Bicycle count")
plt.show()

weekly = data.resample("W").sum()
weekly.plot(style=[':', '--', '-'])
plt.ylabel('Weekly bicycle count')
plt.show()

daily = data.resample('D').sum()
daily.rolling(30, center=True).sum().plot(style=[':', '--', '-'])
plt.ylabel('mean hourly count')
plt.show()

daily.rolling(50, center=True, win_type='gaussian').sum(std=10).plot(style=[':', '--', '-'])
plt.show()
