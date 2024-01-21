import pandas as pd

#this excel file contains 3 level header
df = pd.read_excel('stocks.xlsx', header=[0,1])
print(df)
deStack_df = df.stack()
print(deStack_df)

print(deStack_df.unstack())

df1 = pd.read_excel('stocks_3_levels.xlsx', header=[0,1,2])

#we can stack based on level
print(df1.stack(level=1))

