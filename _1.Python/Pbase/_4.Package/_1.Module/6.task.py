#编写程序fun,其功能下计算下列多项式的和
# f(n) =1 +1/1!+1/2!......1/n!
# 求n等于20时,函数的值
import math
# def fun(n):
#     if n ==1:
#         return 1
#     return n/math.factorial(n)
print(sum(map(lambda x: 1/math.factorial(x),range(0,21))))