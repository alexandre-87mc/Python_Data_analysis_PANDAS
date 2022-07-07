from os import sep
from unicodedata import decimal
import numpy as np
import pandas as pd

#Using read_csv
df = pd.read_csv('C:/Users/alexandre.oliveira/Desktop/exemploCSV.txt',sep=',')
print(df)
print('\n')
df = df+5
print(df)
print('\n')
df.to_csv('C:/Users/alexandre.oliveira/Desktop/exemploCSV2.txt', sep=',', decimal=',')

#Using read_excel
df = pd.read_excel('C:/Users/alexandre.oliveira/Desktop/exemploExcel.xlsx',sheet_name='Sheet1')
print(df)
print('\n')
df = df+50
df.to_excel('C:/Users/alexandre.oliveira/Desktop/exemploExcel2.xlsx', sheet_name='Test1')


#Using read HTML
df = pd.read_html('https://en.wikipedia.org/wiki/Cruzeiro_Esporte_Clube', match='Frigorifico Perrella')
print(df)
print('\n')
