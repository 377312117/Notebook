"""
    此模块示意图形的填充操作
"""



import numpy as np
import matplotlib.pyplot as mp


x = np.linspace(0,8*np.pi,1000)
sinx = np.sin(x)
cosx = np.cos(x/2)/2

mp.figure('Fill',facecolor='lightgray')
# 设置标题
mp.title('Fill',fontsize=18)
# 设置横坐标轴文本
mp.xlabel('X',fontsize=14)
# 设置竖坐标轴文本
mp.ylabel('Y',fontsize=14)
# 设置刻度参数
mp.tick_params(labelsize=10)

mp.plot(x,sinx,color='dodgerblue',label='y=sin(x)')
mp.plot(x,cosx,color='orangered',label=r'$y=\frac{cos(\frac{x}{2})}{2}$')
# 填充
mp.fill_between(
    x,sinx,cosx,sinx>cosx,color='dodgerblue',alpha=0.5
)

mp.tight_layout()
mp.legend()
mp.show()

