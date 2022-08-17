from os import sep
from unicodedata import decimal
import numpy as np
import pandas as pd

#Using read HTML
df = pd.read_html('https://en.wikipedia.org/wiki/Cruzeiro_Esporte_Clube', match='Frigorifico Perrella')
print(df)
print('\n')
