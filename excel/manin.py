import pandas as pd
import os,glob
import numpy as np
path = os.chdir('excel')
files = os.listdir(path)

files_xls = [f for f in files if f[-4:] == 'xlsx']


df = pd.DataFrame()


for f in files_xls:
    data = pd.read_excel(f, header=None)
    df = df.append(data)


escritor = pd.ExcelWriter('output.xlsx')
df.to_excel(escritor,'Hoja1')
escritor.save()