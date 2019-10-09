# -*- coding: utf-8 -*- 
# @Time : 10/9/19 7:42 PM 
# @Author : gordongwb 
# @File : data_split.py

# 分割数据集

import os
from tqdm import tqdm
from sklearn.model_selection import train_test_split
import pandas as pd

data_path = os.path.abspath('..')+'/dataset/mal-api-2019/analysis_data_index.csv'
# data_path = os.path.abspath('..')+'/dataset/mal-api-2019/all_analysis_data.csv'
label_path = os.path.abspath('..')+'/dataset/mal-api-2019/labels.csv'
fast_train = os.path.abspath('..')+'/dataset/fast_train.txt'
fast_test = os.path.abspath('..')+'/dataset/fast_test.txt'
print('reading data ...')
X = pd.read_csv(data_path,header=None)
Y = pd.read_csv(label_path,header=None)
print(X.shape)
print(Y.shape)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, shuffle=True)

with open(fast_train, 'w') as train:
    len = X_train.shape[0]
    for i in range(len):
        text = X_train.iloc[i][0]
        label = Y_train.iloc[i][0]
        train.write('__label__' + label + ' '+text+'\n')

with open(fast_test, 'w') as test:
    len = X_test.shape[0]
    for i in range(len):
        text = X_test.iloc[i][0]
        label = Y_test.iloc[i][0]
        test.write('__label__' + label + ' ' + text+'\n')

