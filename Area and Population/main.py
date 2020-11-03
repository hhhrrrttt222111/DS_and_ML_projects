import pandas as pd


cities = pd.read_csv("california_cities.csv")
print(cities.head())

# extract latitude, longitude, population and area
lat, long = cities["latd"], cities["longd"]
pop, area = cities["population_total"], cities["area_total_km2"]

print(lat)
print(long)
print(pop)
print(area)

print(cities.describe())