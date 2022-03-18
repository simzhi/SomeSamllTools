import pandas as pd
import numpy as np
from datetime import date

today = date.today()
day = today.strftime("%d%m%Y")

newfile = input("Place enter the File name (incloud .xlsm or .Xlsx): \n")

df_scope_new = pd.read_excel(newfile, sheet_name=1, usecols='B:S')
df_scope_new = df_scope_new.drop(labels=[0,1,2], axis=0)
df_scope_new.index = np.arange(0, len(df_scope_new))

df_scope_old = pd.read_excel(newfile, sheet_name=0, usecols='B:S')
df_scope_old = df_scope_old.drop(labels=[0,1,2], axis=0)
df_scope_old.index = np.arange(0, len(df_scope_old))

df_different = df_scope_new.compare(df_scope_old, align_axis=0, keep_equal=True).rename(index={'self': 'New', 'other': 'Old'})

dataname = "Kenzahlkatalog_changes_%s.xlsx" % (day)

df_different.to_excel(dataname)