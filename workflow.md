# 0x00 Data Set Analysis

### Introduction

> This study seeks to obtain data which will help to address machine learning based malware research gaps. The specific objective of this study is to build a benchmark dataset for Windows operating system API calls of various malware. This is the first study to undertake metamorphic malware to build sequential API calls. It is hoped that this research will contribute to a deeper understanding of how metamorphic malware change their behavior (i.e. API calls) by adding meaningless opcodes with their own dissembler/assembler parts.

### Malware Types and System Overall
> In our research, we have translated the families produced by each of the software into 8 main malware families: Trojan, Backdoor, Downloader, Worms, Spyware Adware, Dropper, Virus. Table 1 shows the number of malware belonging to malware families in our data set. As you can see in the table, the number of samples of other malware families except AdWare is quite close to each other. There is such a difference because we don't find too much of malware from the adware malware family.

|Malware Family|Samples|Description|
| ---- | ---- | ---- |
|Spyware|832|enables a user to obtain covert information about another's computer activities by transmitting data covertly from their hard drive.|
|Downloader|1001|share the primary functionality of downloading content.|
|Trojan|1001|misleads users of its true intent.|
|Worms|1001|spreads copies of itself from computer to computer.|
|Adware|379	|hides on your device and serves you advertisements.|
|Dropper|891|surreptitiously carries viruses, back doors and other malicious software so they can be executed on the compromised machine.|
|Virus|	1001|designed to spread from host to host and has the ability to replicate itself.|
|Backdoor|1001|a technique in which a system security mechanism is bypassed undetectably to access a computer or its data.|

>Figure shows the general flow of the generation of the malware data set. As shown in the figure, we have obtained the MD5 hash values of the malware we collect from Github. We searched these hash values using the VirusTotal API, and we have obtained the families of these malicious software from the reports of 67 different antivirus software in VirusTotal. We have observed that the malicious software families found in the reports of these 67 different antivirus software in VirusTotal are different.

![](https://raw.githubusercontent.com/gordongwb/ImageHosting/master/overall.png)

# 0X00 Data PreProcessing

### 数据集转换
对各 API 进行编号，并将由 API 调用顺序组成的原文件转换为由各 API 序号构成的新文件，便于机器学习。

经统计， 在数据集中出现的 API 共有 278 种，存储在 api_dict 中

### 序列长度处理
最长的有 1764421 次 API 调用，最短的只有几百次。
![](https://raw.githubusercontent.com/gordongwb/ImageHosting/master/Screenshot%20from%202019-09-24%2009-32-04.png)

如果将每一个样本都填充到最大值也许将会大大增加算法的复杂度（不一定，需试验）

ref：[几种处理超长序列输入的方法](https://cloud.tencent.com/developer/article/1118259)
# 0x00 Classification Algorithm

### 1.基于术语频率(Term Frequency)的分类

### 2.RNN








