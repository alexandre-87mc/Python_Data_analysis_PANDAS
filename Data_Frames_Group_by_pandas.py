#GroupBY
import pandas as pd
data = {'Company':['GOOG','GOOG','MSFT', 'MSFT','FB','FB'],
'Name':['Sam','Charlie','Amy','Vanessa', 'Carl', 'Sarah'],
'Sell':[200,120,340,124,243,350]}
print(data)

#Create data frame
df = pd.DataFrame(data)
print(df)

#Using groupBY
dfG_com = df.groupby('Company')
dfG_nam = df.groupby('Name')
print(dfG_nam) #Shows only adress
print(dfG_nam) #Shows only adress

#Using sum method
print(dfG_com.sum())
print('\n')
print(dfG_nam.sum())
print('\n')

#Using describe method
print(dfG_com.describe())
print('\n')
print(dfG_nam.describe())
print('\n')

#Using count method
print(dfG_com.count())
print('\n')
print(dfG_nam.count())
print('\n')