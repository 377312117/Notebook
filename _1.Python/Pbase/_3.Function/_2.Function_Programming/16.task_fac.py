#编写程序1~20的阶乘的和
#即:
    #1! +2!+3!......+20!
# def myfac(n):
#     #如果n为1则知道1的阶乘是1,直接返回
#     if n == 1:
#         return 1
#     #否则,进入递推阶段等待下一个结果
#     return n * myfac(n-1)
# n=int(input("请输入:"))

# 方法2:
from math import  factorial as fac
print(sum(map(fac,range(1,4))))