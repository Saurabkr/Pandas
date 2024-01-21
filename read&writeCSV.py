import pandas as pd

#To start reading the CSV file 2 row, use skiprows or header
df = pd.read_csv('stock_data.csv', skiprows=1)
df = pd.read_csv('stock_data.csv', header=1)
# print(df)

#If our CSV is without header: To provide header we use
df = pd.read_csv('stock_data.csv', header=None, names=['ticker','eps','reveue','price','people'])
# print(df)

#if we  want to read only few row
df = pd.read_csv('stock_data.csv', nrows=3)
# print(df)

#cleaning data: replace all n.a. , not available with NaN
df = pd.read_csv('stock_data.csv', na_values=['n.a.','not available'])
# print(df)

#Or replace n.a. , not available with NaN depending upon column
df = pd.read_csv('stock_data.csv', na_values={
    'revenue': ['n.a.','not available',-1],
    'eps' :['n.a.','not available'],
    'price':['n.a.','not available'],
    'people':['n.a.','not available']

})
# print(df)

#####################################################################################################################

#Writing in CSV file

#copying in new csv file
# df.to_csv("new.csv")
#copying with no index
# df.to_csv("new.csv", index=False)

#print only few column
# df.to_csv("new.csv", columns=['eps','revenue'])

#skip to copy header
# df.to_csv("new.csv", header=False)

#Reading & Making change in xlsx file
df = pd.read_excel("stock_data.xlsx")
# print(df)

#Replacing n.a. in people column to some appropriate value
def convert_people_cell(cell):
    if cell == "n.a.":
        return "Sam Walton"
    else:
        return cell

df = pd.read_excel("stock_data.xlsx", converters={
    "people": convert_people_cell
})
print(df)

#copy to new xlsx file
df.to_excel("new.xlsx")
#To add name to sheet1
df.to_excel("new.xlsx", sheet_name='stocks')
#To start from some row and column
df.to_excel("new.xlsx", sheet_name='stocks', startcol=2, startrow=2, index=False)

#To store two data frame in single excel file in different sheet

data_stock = pd.DataFrame({
    'ticker':['GOOGL','WMT','MSFT','RIL'],
    'eps':['27.82','4.61','-1','5.6'],
    'price':['87','76','453','50']
})

data_weather = pd.DataFrame({

    'Country':['India','Australlia','U.S.A','France'],
    "temperature":[23,25,1,-1]

})

with pd.ExcelWriter('stocks_weather.xlsx') as writter:
    df.to_excel(writter, sheet_name='stock', index=False)
    df.to_excel(writter, sheet_name='weather', index=False)




