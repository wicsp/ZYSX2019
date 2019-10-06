# ZYSX2019

> 本项目用于2019年下半学期的专业实训团队协作

本项目旨在实现通过机器学习的方式，对恶意软件进行分类。

本项目使用的主要语言为 `Python` , 基于 `Tensorflow` 和 `Keras` 进行机器学习。

数据集来源 https://github.com/ocatak/malware_api_class

### 第一阶段

- 了解原数据集的数据来源和处理方式

  - lables.csv 中有 7107 行， 对应 mal-api-2019.zip 解压后的7107行数据。（请在 `.gitignore` 文件中加入解压后的txt文件，不要上传到github上）
 
- 通过三种常见的文本处理算法（RNN，LSTM，GRU），对数据进行初步学习

- 通过比较上面三中文本处理算法得到的训练模型的多个指标（precision，recall，accuracy，specificity，ROC/AUC...），选出两个指标显示情况较好的算法

 第五（六）周汇报 ppt制作

### 第二阶段
*** 在原算法的基础上对改进算法进行测试

*** 特征提取