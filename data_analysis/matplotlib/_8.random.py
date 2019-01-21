import numpy as np
import matplotlib.pyplot as mp


n = 1000
x = np.random.normal(172,20,n)
y = np.random.normal(60,10,n)


mp.figure(
    'Persons',
    facecolor='lightgray',
)

mp.title('Persons')
# 设置横坐标轴文本
mp.xlabel('Height',fontsize=14)
# 设置竖坐标轴文本
mp.ylabel('Weight',fontsize=12)
mp.tick_params(labelsize=12)

d = (x-172)**2 +(y-60)**2
mp.scatter(x,y,c=d, cmap='jet',s=40)

mp.tight_layout()
mp.show()