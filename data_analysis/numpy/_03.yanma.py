"""
    此示例示意掩码
"""

import numpy as np



a = np.array(
    [1,2,3,4,5,6,7,8,]
)

f = np.array(
    [True,False,True,False,True,False,True,False,]
)
# 将Fasle对应的元素进行掩盖,形成新的数组
print(a[f])
# [1 3 5 7]

# 将数组每个元素与3进行比较,留下符合的元素
print(a[a >3])

# 打印1~100中3的倍数或者7的倍数都打印出来

b = np.arange(1,100)
flag_b1 = b % 3 == 0
flag_b2 = b % 7 == 0 
print(flag_b1)
print(flag_b2)
flag = np.any(
    [
        flag_b1,
        flag_b2,
    ],
    axis=0
)
print(b[flag])
