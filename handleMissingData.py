import pandas as pd 

df = pd.read_csv("weather_data1.csv", parse_dates=['day'])
df.set_index('day', inplace=True)
print(df)

#Convert all NaN value to 0
new_df = df.fillna(0)
print(new_df)

#if we want to insert NaN to any other value based on column
new_def = df.fillna({
    'event':'Not Event',
    'windspeed': 0,
    'temperature':0
}) 
print(new_def)

#we can also replace NaN from forward or backward day's data
#forwaerdcell value got filled
new_df = df.fillna(method="ffill")
#backcell value got filled
new_df = df.fillna(method='bfill')
#formward column cell value get filled
new_df = df.fillna(method='ffill', axis='columns')
#forward row value filled with limit=1
new_df = df.fillna(method="ffill", limit=1)

#fill the NaN with more precise value
new_df = df.interpolate()
print(new_df)
new_df = df.interpolate(method='time')
print(new_df)

#how to drop row containing NaN cell
drp_df = df.dropna()
print(drp_df)

#how to drop row with all cell value as NaN
drp_df = df.dropna(how='all')
print(drp_df)

#How to drop row not containong atleast 2 non-NaN 
drp_df = df.dropna(thresh=2)
print(drp_df)

