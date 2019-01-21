"""
演示三维数组
"""

import numpy as np


a = np.arange(1,7).reshape((2,3)) # 参数中前面是每一行个数,后面是维度
b= np.arange(7,13).reshape((2,3))

# 垂直方向操作
c = np.vstack((a,b))
print('c:',c)

a,b = np.vsplit(c,2)  # 拆成2份
print('垂直a,b:',a,'\n',b)


# 水平方向操作
d  =  np.hstack((a,b))
a,b = np.hsplit(d,2)
print('水平a,b:',a,'\n',b)


e  =  np.dstack((a,b))
a,b = np.dsplit(e,2)
print('深度a,b:',a,'\n',b)


a = a.reshape(3,2)
b= b.reshape(3,2)
print(a,'\n',b)
c=np.concatenate((a,b),axis=1)
print('c:',c)

# 通过给定的axis轴向与拆封的份数对c数组进行拆分
np.split(c,2,axis=0)

