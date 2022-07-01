#GroupBY
import pandas as pd
data = {'Empresa':['GOOG','GOOG','MSFT', 'MSFT','FB','FB'],
'Nome':['Sam','Charlie','Amy','Vanessa', 'Carl', 'Sarah'],
'Venda':[200,120,340,124,243,350]}
print(data)

#Create data frame
df = pd.DataFrame(data)
print(df)