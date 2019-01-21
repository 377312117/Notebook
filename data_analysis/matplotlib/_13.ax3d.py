"""
绘制3d图

"""

import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d


n=100
x=np.random.normal(0,1,n)
y=np.random.normal(0,1,n)
z=np.random.normal(0,1,n)

mp.figure('3Dpoint',facecolor='lightgray')
mp.title('3Dpoint',fontsize=18)

ax = mp.gca(projection='3d')

# 设置横坐标轴文本
ax.set_xlabel('X',fontsize=14)
# 设置竖坐标轴文本
ax.set_ylabel('Y',fontsize=14)
# 设置竖坐标轴文本
ax.set_zlabel('Z',fontsize=14)
# 设置刻度参数
mp.tick_params(labelsize=10)


v = np.sqrt(x**2+y**2+z**2)
ax.scatter(x,y,z,s=60,cmap='jet',c=v,alpha=0.5)
mp.show()