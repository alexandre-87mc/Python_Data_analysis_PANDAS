import numpy as np
import pandas as pd

#Make random equal in every PC
np.random.seed(101)

#Create a Data Frame
df = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)

#Playing with conditions
print(df>0)

#Create data frame with condition
bol = df > 0
print(bol)
print(df[bol])

#Print lines that have the column 'W' value greater than 0
print(df[df['W']>0])

#Print lines of colunm 'Y' that have the column 'W' value greater than 0
print(df[df['W']>0]['Y'])

#Using multiple conditions
df2 = df[(df['W']>0) & (df['Y']>1)]
print(df2)

#reset index
print(df.reset_index())
print(df)
print(df.reset_index(inplace=True))
print(df)

#changing index
col = 'RS RJ SP AM SC'.split()
print(col)
df['Estado'] = col
df.set_index('Estado', inplace=True)
print(df)