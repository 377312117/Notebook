#求1**2+2**2+3**2........9**2的和
def pow2(x):
    return x**2
# s=0
# for x in map(pow2,range(1,10)):
#     s += x
# print(s)
# 方法2
m = map(pow2,range(1,10))
print(sum(m))
#map得到的数据也是可迭代对象