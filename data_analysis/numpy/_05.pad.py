# 测试不同长度的数组的组合

import numpy as np

a = np.arange(1,7)
b = np.arange(10,16)
c = np.pad(b,pad_width=(0,1),mode='constant',constant_values=-1)

print(a)
print(b)
print(c)
