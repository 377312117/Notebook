#1.写一个函数isprime(x)判断x是否是素数,如果是返回True,否则返回False.
def isprime(x):
    #如果x<2不是素数
    if x<2:
        return False
    for i in (2,x):
        if x % i ==0:
            return False
        else:
            return True
s=int(input("请输入一个正整数:"))
print(isprime(s))