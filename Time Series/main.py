import pandas as pd


data = pd.read_csv("fremont-bridge.csv", index_col='Date', parse_dates=True)
# print(data.head())

# Renaming Columns
data.columns = ["West", "East"]
data["Total"] = data["West"] + data["East"]
print(data.head())

print(data.dropna().describe())
