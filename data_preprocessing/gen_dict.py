# -*- coding: utf-8 -*- 
# @Time : 9/23/19 3:35 PM 
# @Author : kzl 
# @File : gen_dict.py

import time
import csv
import os


list = []

start = time.time()
with open(os.path.abspath('.')+'/dataset/mal-api-2019/all_analysis_data', 'r') as old_f:
    i = 0
    while True:
        line = old_f.readline()
        if line:
            print(i)
            i += 1
            api = ''
            for char in line:
                if char != ' ':
                    api += char
                else:
                    if api not in list:
                        list.append(api)
                    api = ''
        else:
            break

list.sort()
print('number of api:{0}'.format(len(list)))
finish = time.time()

api_dict = {}
index = 1
for i in list:
    api_dict[index] = i
    index += 1
with open('api_dict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(api_dict.items())


print('time:{0}'.format(finish-start))






