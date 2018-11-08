# 此示例示意 用生成器函数创建从0到n的一系列整数(不包含n)
def myinteger(n): 
    i = 0    # 设置初始值为0
    while i < n:
        yield i    # 生成i给next(it) 调用
        i += 1     # 为生成下一个数做准备

for x in myinteger(5):   # for语句的本质,就是调用next语句
    print(x)
