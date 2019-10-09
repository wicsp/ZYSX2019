# -*- coding: utf-8 -*- 
# @Time : 9/23/19 5:27 PM 
# @Author : kzl 
# @File : test.py

import pandas as pd

df = pd.DataFrame([9,2,3,5])
print(df.shape)
df.to_csv('test.csv',index=False,header=False)

df2 = pd.read_csv('test.csv',header=None)
print(df2.shape)
# print(df2)
len = df2.shape[0]
print(len)
for i in range(len):
    print(i)
    print(df2.iloc[i][0])