import numpy as np
import pandas as pd

#Index levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

#Create Data Frame
df = pd.DataFrame(np.random.randn(6,2),index=hier_index, columns=['A','B'])
print(df)

#Access items
print(df.loc['G1'])
print(df.loc['G1'].loc[1])

#Giving names to index
df.index.names = ['Grupo','Numero']
print(df)

#Using xs command
print(df.xs(1,level='Numero'))