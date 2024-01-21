import pandas as pd
import numpy as np

df = pd.read_csv("weather_data2.csv")
print(df)

#replace all -99999 value from NaN
new_df = df.replace([-99999,0],np.NaN)
print(new_df)

#replace all -99999 to NaN and 0 to NaN based on column
new_df = df.replace({
    "temperature": -99999,
    "windspeed":-99999,
    "event":'0'
}, np.NaN)

print(new_df)

#we can also replace particular cell value via mapping
new_df = df.replace({
    -99999: np.NaN,
    '0': 'No Event'
})

print(new_df)

#If the data includes unit then to remove unit we need
# new_df = df.replace('[A-Za-z]', '', regex=True)
# print(new_df)#it remove all the event column data which contain A-Z a-z

new_df = df.replace({
    "temperature":'[A-Za-z]',
    "windspeed":'[A-Za-z]'
}, '', regex=True)

print(new_df)

#Replace any column data to number

df = pd.DataFrame({
    "Score":['average', 'good','exceptional'],
    "Student":['sonu','monu','memo']
})
print(df)

new_df = df.replace(['average', 'good','exceptional'],[1,2,3])
print(new_df)


