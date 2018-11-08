# 给一个整数n,用一个函数来计算
# 1+2**2+3**3......n**n的和
# n给一个小点的数
def mysum(n):
    s=0
    for i in range(1,n+1):
        s+=i**i
    return s
a=int(input("please input a number:")) 
print(mysum(a))

# 方法2
def f(n):
    return sum(map(lambda x : x**x,range(1,n+1)))

