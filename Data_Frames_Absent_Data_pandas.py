#ABSENT DATA

import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan], 'B':[5, np.nan, np.nan], 'C':[1,2,3]}
print(d)
df = pd.DataFrame(d)
print('\n')
print(df)

#Using dropna
print('\n')
print(df.dropna())
print('\n')
print(df.dropna(thresh=2))

#Using fillna
print('\n')
print(df.fillna(value=df)) #NOT USEFULL LIKE THIS
print('\n')
print(df['A'].fillna(value=df['A'].mean()))
print('\n')
print(df.fillna(method='ffill'))