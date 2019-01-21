import numpy as np
import matplotlib.pyplot as mp

mp.figure(
    'Figure1',
    figsize=(4,3),
    facecolor='lightgray',
)

mp.figure(
    'Figure2',
    figsize=(4,3),
    facecolor='black',
)

# 选择窗口
mp.figure('Figure1')
# 设置标题
mp.title('Figure1',fontsize=18)
# 设置横坐标轴文本
mp.xlabel('Date',fontsize=12)
# 设置竖坐标轴文本
mp.ylabel('Price',fontsize=12)
# 设置刻度参数
mp.tick_params(labelsize=8)
# 设置图标网格线
mp.grid(linestyle=':')
# 设置紧凑布局
mp.tight_layout()
mp.show()