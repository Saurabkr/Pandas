import pandas as pd

IndWeather = pd.DataFrame({
    "city": ['Mumbai', 'Delhi', 'Banglore'],
    "temperature":[20,30,40]
}) 
IndiaWeather2 = pd.DataFrame({
    "city": ['Mumbai', 'Delhi', 'Banglore'],
    "temperature":[20,30,40]
})

IndWeather1 = pd.DataFrame({
    "city": ['Mumbai', 'Delhi','Pune'],
    "wind speed":[67,30,45]
})

#It perform intersector or inner join 
new_merge = pd.merge(IndWeather,IndWeather1, on='city')
print(new_merge)

#To make it union or outter join 
new_merge1 = pd.merge(IndWeather,IndWeather1, on='city', how='outer')
print(new_merge1)

#Left and right join
new_mergeLeft = pd.merge(IndWeather,IndWeather1, on='city', how='left')
print(new_mergeLeft)

#Indicator : use to indicate that data come from which table
new_mergeRight = pd.merge(IndWeather,IndWeather1, on='city', how='right', indicator=True)
print(new_mergeRight)

#To merge two CSV with same col
new_mergesame = pd.merge(IndWeather,IndiaWeather2, on='city', suffixes=('left','right'))
print(new_mergesame)