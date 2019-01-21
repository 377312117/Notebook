"""
    示意加载文件到图像中
"""

import numpy as np
import matplotlib.pyplot as mp
import datetime as dt


# 定义函数,转换日期格式
def dmy2ymd(dmy):
    dmy = str(dmy,encoding='utf-8')
    date = dt.datetime.strptime(
        dmy,'%d-%m-%Y'
    ).date()
    str1 = date.strftime('%Y-%m-%d')
    return str1

# 加载文件
dates=np.loadtxt(
    './aapl.csv',
    delimiter=',',
    usecols=(1,2,3,4,5,6),
    unpack=True,
    dtype='M8[D],f8,f8,f8,f8',
    converters = {1:dmy2ymd},
)
print(dates)




