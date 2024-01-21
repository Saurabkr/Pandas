import pandas as pd

df = pd.read_csv("weather.csv")
print(df)

new_df = pd.melt(df,id_vars='day')
print(new_df)
print(new_df[new_df['variable']=='chicago'])
print(pd.melt(df, id_vars='day', var_name='city', value_name='temperature'))