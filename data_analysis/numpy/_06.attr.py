"""
测试数组的属性
"""

import numpy as np

a = np.array(
    [
        [1+1j,2+4j,3+7j],
        [4+2j,5+5j,6+8j],
        [7+3j,8+6j,9+9j],
    ]
)

print(f'a.dtype:{a.dtype},a.ndim:{a.ndim}')
print(a.real)
print(a.imag)
print(a.imag.T)
c  = a[:,:2]
print(c)
print(c.T)
