# -*- coding: utf-8 -*- 
# @Time : 9/24/19 8:58 AM 
# @Author : gordongwb 
# @File : find_lenth.py

# 计算长度并找到最长的 api 序列

import os
import time

start = time.time()
length = 0
row = 0
wubai = 0
with open(os.path.abspath('..')+'/dataset/mal-api-2019/analysis_data_index.csv') as f:
    while True:
        line = f.readline()
        if line:
            row += 1
            list = line.split(' ')
            if len(list) > length:
                length = len(list)
                print(row)
                print(length)
            if len(list) > 10000:
                wubai += 1
        else:
            break
print("test:{0}".format(wubai))
print(row)
print('length:{0}'.format(length))
