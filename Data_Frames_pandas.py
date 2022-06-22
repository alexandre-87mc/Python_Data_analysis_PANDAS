#DATA FRAMES
from traceback import print_tb
import pandas as pd 
import numpy as np 

#Make random equal in every PC
np.random.seed(101)

#Create a Data Frame
df = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)
print(df[['W','Z']])

#Create new column
df['new'] = df['W']+df['X']
print(df['new'])

#new column is now part of df
print(df)

#Obs. You can use df.W to call, but this may cause confusion with methods
print(df.new) #AVOID USING THIS

#Remove column using drop
print(df.drop('new',axis=1))
#'new' is inside df yet
print(df)
#THIS IS HOW WE REMOVE THE COLUMN 'new'
df = df.drop('new', axis=1)
print(df)
df['new'] = df['W']+df['X']
print('\nColumn "new" added again\n')
print(df)
#WE CAN USE 'implace' METHOD TOO
df.drop('new',axis=1, inplace=True)
print('\n')
print(df)

#Location using 'loc' and 'iloc'
print(df.loc['A','W'])
print(df.loc[['A','B'],['X','Y','Z']])
print(df.iloc[0:4,2:])