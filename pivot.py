import pandas as pd
import numpy as np
df=pd.read_csv("C:/Users/SPTINT-12/Downloads/Department_Dataset.csv")
print(df)
pivot=df.pivot_table(index=['name'],values=['salary'],aggfunc='sum')
print(pivot
        )
output
name
angel     100000
brandon    54000
dennis     48000
douglas    50000
frances   690000
gary       87000
jerry      25000
julie      56000
kimberly  560000
