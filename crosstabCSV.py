import pandas as pd
import numpy as np

df = pd.read_excel("survey.xls")
print(df)

new_df = pd.crosstab(df.natinality, df.Handedness)
#data with two header
new_df = pd.crosstab([df.natinality,df.Handedness], df.sex)
#Dta with total col
new_df = pd.crosstab([df.natinality,df.Handedness], df.sex , margins=True)
#Data with percentage
new_df = pd.crosstab([df.natinality,df.Handedness], df.sex, normalize='index')
#data wih average
new_df = pd.crosstab(df.sex ,df.Handedness, values=df.Age, aggfunc=np.average)