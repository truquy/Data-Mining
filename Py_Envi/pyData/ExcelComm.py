import pandas as pd
import numpy as np

pathFile = r'C:\Users\tquy8\Desktop\Table01.xlsx'
# Replace '\' by '/'
path = pathFile.replace(' \ ', ' / ')
data = pd.read_excel(path)
data = pd.DataFrame(data)

pd = pd.DataFrame(data)

print (pd)
