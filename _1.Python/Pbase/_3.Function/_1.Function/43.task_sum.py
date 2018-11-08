#给出一个整数n,写一个函数计算
# 1+2+3+4+5+6+7+8+9....+n的值来返回结果并要求用函数来做
# 如:
def mysum(n):
    s=0
    for i in range(n+1):
        s+=i
    return s
print(mysum(100))   #5050
print(mysum(10))    #55
