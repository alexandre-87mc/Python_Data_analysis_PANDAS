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

#Using apply
def times2(x):
    return x*2
print(df['col1'].apply(times2))
print('\n')

#Delete column
#del df['col2'] #To use it again remove '#'
print(df)
print('\n')

#Values of columns or index
print(df.columns)
print(df.index)
print('\n')

#Order values
#df.sort_values(by='col2', inplace=True) #To use it again remove '#'
print(df)
print('\n')

#Check if df is null
df.isnull
print(df)
print('\n')

#Erase Nam values
df.dropna()
print(df)
print('\n')

#Fill values to df
print(df['col1'].fillna(value=df['col1'].mean()))

#Pivot tables
data = {'A':['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B':['one', 'one', 'two', 'two', 'one', 'one'],
        'C':['x', 'y', 'x', 'y', 'x', 'y'],
        'D':[1,3,2,5,4,1]}

df_PVT = pd.DataFrame(data)
print(df_PVT)
print('\n')

print(df_PVT.pivot_table(values='D', index=['A','B'], columns='C'))

