# -*- coding: utf-8 -*- 
# @Time : 9/23/19 6:28 PM 
# @Author : gordongwb
# @File : transform.py

import os
import time
import csv

start = time.time()
with open(os.path.abspath('..')+'/api_dict.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    api_dict = dict(reader)
    print(api_dict)
new_dict = { v : k for k,v in api_dict.items() }
with open(os.path.abspath('..')+'/dataset/mal-api-2019/all_analysis_data', 'r') as old_f:
    with open(os.path.abspath('..')+'/dataset/analysis_data_index', 'w') as new_f:
        i=0
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
                        index = new_dict[api]
                        new_f.write(index+' ')
                        api = ''
                new_f.write('\n')
            else:
                break

finish = time.time()
print('time:{0}'.format(finish-start))
