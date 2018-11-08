#写一个函数生成器,myxrange(start,stop,step) 来生成一系列整数
# 要求和range功能完全一致
# 不允许使用让range函数和列表
# 然后用自己写的函数求1~100之间的奇数的平方和
def myxrange(start,stop,step=1):
    if stop is None:
        stop = start
        start = 0
    if step > 0:
        while start < stop:
            yield start
            start+=step
    elif step < 0: 
        while start > stop:
            yield start
            start+=step
    else:
        return
print(sum(x**2 for x in myxrange(1,100,2)))