#SERIES

import numpy as np
import pandas as pd 

#Create material
labels1 = ['a','b','c']
my_list1 = [10,20,30]
arr1 = np.array([10,20,30])
d1 = {'a':10, 'b':20, 'c':30}

#Creating SERIES
series1 = pd.Series(data=my_list1, index=labels1)
print(series1)
print(series1['b'])

print('\n')

series2 = pd.Series(my_list1, labels1)
print(series1)
print(series1['b'])

print('\n')

series3 = pd.Series(labels1, my_list1)
print(series3)
print(series3[20])

print('\n')

series4 = pd.Series(labels1, arr1)
print(series4)
print(series4[20])

print('\n')

#Making operations
series5 = pd.Series([1,2,3,4], index = ['EUA','GERMANY','URSS','JAPAN'])
print(series5)
print('\n')
series6 = pd.Series([1,2,3,4], index = ['EUA','GERMANY','ITALY','JAPAN'])
print(series6)
print('\n')
print(series5+series6)