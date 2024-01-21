import pandas as pd

df = pd.read_csv('weather_by_cities.csv')
print(df)

#group by seggregate the csv data based on city then find the max,min and mean
new_df = df.groupby('city')
print(new_df.max())
print(new_df.mean())
print(new_df.describe())


