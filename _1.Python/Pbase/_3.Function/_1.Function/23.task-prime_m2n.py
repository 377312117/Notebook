#写一个函数prime_m2n(m,n),返回从m开始,到n结束范围内的素数并打印
def isprime(x):
    #如果x<2不是素数
    if x<2:
        return False
    for i in (2,x):
        if x % i ==0:
            return False
        return True
# s=int(input("请输入一个正整数:"))
# print(isprime(s))
def prime_m2n(m,n):
    L=[]
    for y in range(m,n):
        if isprime(y):
            L.append(y)
    return L
a=int(input("请输入一个正整数:"))
b=int(input("请输入一个正整数:"))
print(prime_m2n(a,b))