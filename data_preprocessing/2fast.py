# -*- coding: utf-8 -*- 
# @Time : 10/6/19 6:16 PM 
# @Author : gordongwb 
# @File : 2fast.py

# 将数据和标签转化为 FastText 支持的格式

import os
from tqdm import tqdm

path = os.path.abspath('..')
pbar = tqdm(total=7107)
with open(path+'/dataset/labels.csv', 'r') as labels:
    with open(path+'/dataset/mal-api-2019/all_analysis_data.csv', 'r') as data:
        with open(path+'/dataset/train_fast', 'w') as train:
            while True:
                label = labels.readline()
                text = data.readline()
                if label and text:
                    train.write('__label__'+label+' '+text+'\n')
                    pbar.update(1)
                else:
                    break

pbar.close()