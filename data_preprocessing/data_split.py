# -*- coding: utf-8 -*- 
# @Time : 10/9/19 7:42 PM 
# @Author : gordongwb 
# @File : data_split.py

# 分割数据集

import os
from tqdm import tqdm
from sklearn.model_selection import train_test_split
import pandas as pd

data_path = os.path.abspath('..')+'/dataset/mal-api-2019/all_analysis_data.csv'
label_path = os.path.abspath('..')+'/dataset/mal-api-2019/labels.csv'
X = pd.read_csv(data_path)
print(X.shape)
print(X[0][0])
