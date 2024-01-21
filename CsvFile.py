import pandas as pd 

df = pd.read_csv('weather_data.csv')

print(df)
# print(df.to_string())

#Use to print first few row if we have large data set
print(df.head())
#Use to print last few row if we have large data set
print(df.tail())

#Slicing & indexing
print("Example of slicing: \n",df[0:5:2]) #start:end:step

#Printing selected columns
print("To print number of column\n",df.columns)
print('Print only event column \n',df['event'])
print("Printing only selected columns\n",df[['event','temperature']])
print("Print the event & day column's 0-3rd row:\n",df[['event','day']][0:4])

#Operations on csv file
print("Print maximum tempurature :\n",df['temperature'].max())
print("print minimum temp :\n",df['temperature'].min())
print("print mean of temp:\n",df['temperature'].mean())
print("Print standard deviation :\n",df['temperature'].std())
print("print all the statistics\n",df['temperature'].describe())

#Condition on file
print("Print on whic day temperature is maximum\n",df['day'][df.temperature==df.temperature.max()])#we can use df.temperature in case when there is no space with words, or else we have to use df['temperature']

#How to Set index 
df.set_index('day', inplace=True)
print('To set index:\n',df)
print('Exact data based on day:\n',df.loc['1/2/2017'])

#to reset the index
df.reset_index(inplace=True)
print('Reset original index:\n',df)




