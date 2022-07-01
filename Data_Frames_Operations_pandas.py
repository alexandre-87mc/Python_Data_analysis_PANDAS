#Pandas operations
import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())

#Unique data selection
print(df['col2'].unique())
print('\n')
#Similar numpy unique method
import numpy as np
print(np.unique(df['col2']))
print('\n')
#Number of unique values
print(df['col2'].nunique())
print('\n')

#Value counts
print(df['col2'].value_counts())
print('\n')

#Find a Dataframe with booleans
print(df[(df['col1']>2)])
print('\n')
print(df[(df['col1']>2) & (df['col2']>500)])
print('\n')

def times2():
    return x*2


