import numpy as np
import matplotlib.pyplot as mp


apples = [23,66,12,28,23,21,29,43,45,23,76,89]
oranges = [63,36,18,38,83,71,99,13,45,73,26,59]


mp.figure('Bar',facecolor='lightgray')
mp.title('Bar',fontsize=18)
# 设置横坐标轴文本
mp.xlabel('Month',fontsize=14)
# 设置竖坐标轴文本
mp.ylabel('Price',fontsize=14)
# 设置刻度参数
mp.tick_params(labelsize=10)
mp.grid(linestyle=':',axis='y')

# 设置坐标范围
x = np.arange(len(apples))
# 描绘柱状图
mp.bar(
    x,
    apples,
    0.4,
    color='dodgerblue',
    label='Apple'
)

mp.bar(
    x,
    oranges,
    0.4,
    color='orangered',
    label='Orange',
)

# 为坐标增加刻度名称
mp.xticks(x,['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])


mp.legend()
mp.show()
