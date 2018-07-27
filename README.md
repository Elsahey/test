# test
daf
```python

data_re['BMI_nor'] = (data_re['BMI_assess'].max() - data_re['BMI_assess'])/(data_re['BMI_assess'].max()-data_re['BMI_assess'].min())
data_re['leg_nor'] = (data_re['leg_assess'] - data_re['leg_assess'].min())/(data_re['leg_assess'].max()-data_re['leg_assess'].min())              
data_re['arm_nor'] = (data_re['arm_assess'].max() - data_re['arm_assess'])/(data_re['arm_assess'].max()-data_re['arm_assess'].min()) 
data_re['age_nor'] = (data_re['age_assess'].max() - data_re['age_assess'])/(data_re['age_assess'].max()-data_re['age_assess'].min())

data_re['final'] = (data_re['BMI_nor']+data_re['leg_nor']+data_re['arm_nor']+data_re['age_nor'])/4

plt.figure(figsize = (10,6))
data_re.sort_values(by = 'final',inplace = True,ascending=False)
data_re.reset_index(inplace=True)

data_re[['age_nor','BMI_nor','leg_nor','arm_nor']].plot.area(colormap = 'PuRd',alpha = 0.5,figsize = (10,6))
plt.ylim([0,4])
plt.grid(linestyle = '--')

datatop8 = data_re[:8]

fig = plt.figure(figsize=(18,8))
plt.subplots_adjust(wspace=0.35,hspace=0.5)
'''


'''python
import requests #用来访问网页的库，好比浏览器
from bs4 import BeautifulSoup #爬虫库，用来抓取网页中的信息，它有一个可爱的名字beautifulsoup,寓意一碗浓汤，我要从汤中捞出不同的美味
import time #时间模块，为了控制爬虫速度，防止由于速度过快，被 ban IP
import csv #用来操作csv的库，这次用来创建表格，存储数据
'''
