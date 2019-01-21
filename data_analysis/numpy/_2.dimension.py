import numpy as np

a = np.arange(1,9)

# 视图变维使用的还是原始数组的数据,如果修改了原始数组中的数据,那么新数组读到
# 的数据也会发生变化
b = a.reshape((2,4))
print(b,a)

a[0] = 999
print(b)
c= b.ravel()
print(c)



d = b.flatten()
d[0] = 110
print(d,a)
