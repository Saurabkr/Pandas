import pandas as pd

df = pd.read_csv("weather_by_cities.csv")
print(df)

new_df=df.pivot(index='day', columns='city',values=['temperature','event'])
print(new_df)

#Pivot table: use to summerize the two value if we have city with two temperature of same date, it return mean
df1 = pd.read_csv("weather2.csv")
print(df1)

#by default it calculate mean
new_df1=df1.pivot_table(index='city', columns='date')
print(new_df1)

#we can also change the aggregated function to be sum like:
new_df1=df1.pivot_table(index='city', columns='date', aggfunc='sum')
print(new_df1)

#to find the avg of what we get above:
new_df1=df1.pivot_table(index='city', columns='date', margins=True)
print(new_df1)

#To use grouper
df2 = pd.read_csv("weather3.csv")
df2['date'] = pd.to_datetime(df2['date'])
print(df2)

new_df3 = df2.pivot_table(index=pd.Grouper(freq='M', key='date'),columns='city')
print(new_df3)
