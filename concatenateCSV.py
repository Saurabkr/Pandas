import pandas as pd

IndWeather = pd.DataFrame({
    "city": ['Mumbai', 'Delhi', 'Banglore'],
    "temperature":[20,30,40],
}) 
print(IndWeather)

USAWeather = pd.DataFrame({
    "city": ['New Nork', 'Boston', 'Chicago'],
    "temperature":[-2,3,6]
})

#we get concatenated CSV file with include indexes
new_df = pd.concat([IndWeather,USAWeather])
#To remove index and make it consecutive
new_df = pd.concat([IndWeather,USAWeather], ignore_index=True)
print(new_df)

#to concatenate using keys
new_df = pd.concat([IndWeather,USAWeather], keys=['India','U.S.A'])
print(new_df)
#to get the india data
print(new_df.loc['India'])

#If we want to append the column
IndWeather1 = pd.DataFrame({
    "city": ['Mubmai', 'Delhi','Banglore'],
    "wind speed":[39,31,47]
})

IndWeathrSeries = pd.Series(['Humid','Cold', 'Windy'], name="Event")

newDf = pd.concat([IndWeather, IndWeather1], axis=1)
print(newDf)

new__Df = pd.concat([IndWeather, IndWeathrSeries], axis=1)
print(new__Df)