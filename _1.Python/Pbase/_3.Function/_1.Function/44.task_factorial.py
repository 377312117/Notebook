#给一个整数n,写一个函数的来计算阶乘n!
#n!=1*2*3*4*5*........n
def myfac(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
print(myfac(5))   #120
#方法2 递归阶乘
# 分析:
# 5!=5*4!
# 4=4*3!
# .....
def myfac(n):
    #如果n为1则知道1的阶乘是1,直接返回
    if n == 1:
        return 1
    #否则,进入递推阶段等待下一个结果
    return n * myfac(n-1)
print(myfac(5))   #???

