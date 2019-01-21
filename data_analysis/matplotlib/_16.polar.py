"""
    绘制极坐标系
"""

import numpy as np
import matplotlib.pyplot as mp


x = np.linspace(0,4*np.pi,1000)
y = 0.8*x

# 设置为极坐标系
mp.figure('Polar',facecolor='lightgray')
mp.gca(projection='polar')



mp.title('Polar',fontsize=18)
# 设置横坐标轴文本
mp.xlabel('X',fontsize=14)
# 设置竖坐标轴文本
mp.ylabel('Y',fontsize=14)
# 设置刻度参数
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

mp.plot(x,y,label='y=0.8x')
mp.legend()
mp.show()
